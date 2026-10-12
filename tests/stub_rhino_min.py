# -*- coding: utf-8 -*-
"""Stub minimo de Rhino.Geometry para ejecutar los componentes GHPython
   (LADOS v06 / PATIO v02) con geometria de polilineas en CPython (solo tests)."""
import math


class Point3d(object):
    __slots__ = ('X', 'Y', 'Z')

    def __init__(self, x=0.0, y=0.0, z=0.0):
        if isinstance(x, Point3d):
            self.X, self.Y, self.Z = x.X, x.Y, x.Z
        else:
            self.X = float(x)
            self.Y = float(y)
            self.Z = float(z)

    def DistanceTo(self, o):
        return math.sqrt((self.X - o.X) ** 2 + (self.Y - o.Y) ** 2 + (self.Z - o.Z) ** 2)

    def __repr__(self):
        return 'P({:.3f},{:.3f})'.format(self.X, self.Y)


class Vector3d(object):
    __slots__ = ('X', 'Y', 'Z')

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.X = float(x)
        self.Y = float(y)
        self.Z = float(z)

    @property
    def Length(self):
        return math.sqrt(self.X * self.X + self.Y * self.Y + self.Z * self.Z)

    def Unitize(self, tol=1e-12):
        L = self.Length
        if L <= tol:
            return False
        self.X /= L
        self.Y /= L
        self.Z /= L
        return True


class Polyline(object):
    def __init__(self, points=None):
        self._pts = []
        if points:
            for p in points:
                self.Add(p)

    def Add(self, a, b=None, c=None):
        if isinstance(a, Point3d):
            self._pts.append(a)
        elif b is None and c is None:
            # Assume it's a tuple/list of coordinates
            self._pts.append(Point3d(a))
        else:
            self._pts.append(Point3d(a, b, c))

    @property
    def Count(self):
        return len(self._pts)

    def __getitem__(self, i):
        return self._pts[i]

    def __len__(self):
        return len(self._pts)

    @property
    def IsClosed(self):
        if len(self._pts) < 2:
            return False
        return self._pts[0].DistanceTo(self._pts[-1]) < 1e-8


class PolylineCurve(object):
    def __init__(self, poly):
        if isinstance(poly, Polyline):
            self._pts = [Point3d(p) for p in poly._pts]
        elif isinstance(poly, PolylineCurve):
            self._pts = [Point3d(p) for p in poly._pts]
        else:
            self._pts = [Point3d(p) if isinstance(p, Point3d) else Point3d(*p) for p in poly]
        self._seglens = []
        self._cum = [0.0]
        self._total = 0.0
        for i in range(len(self._pts) - 1):
            L = self._pts[i].DistanceTo(self._pts[i + 1])
            self._seglens.append(L)
            self._total += L
            self._cum.append(self._total)

    # ---------- API estilo RhinoCommon ----------
    def ClosestPoint(self, pt, tol=0.0):
        if self._total <= 0.0:
            return (False, 0.0)
        best_t = None
        best_d = None
        for i in range(len(self._pts) - 1):
            a, b = self._pts[i], self._pts[i + 1]
            dx = b.X - a.X
            dy = b.Y - a.Y
            l2 = dx * dx + dy * dy
            if l2 < 1e-18:
                t = 0.0
            else:
                t = ((pt.X - a.X) * dx + (pt.Y - a.Y) * dy) / l2
                if t < 0.0:
                    t = 0.0
                elif t > 1.0:
                    t = 1.0
            cx = a.X + t * dx
            cy = a.Y + t * dy
            d = (pt.X - cx) ** 2 + (pt.Y - cy) ** 2
            if best_d is None or d < best_d:
                best_d = d
                best_t = self._cum[i] + t * self._seglens[i]
        return (True, best_t)

    def PointAt(self, t):
        if self._total <= 0.0:
            return Point3d(0, 0, 0)
        if t < 0.0:
            t = 0.0
        if t > self._total:
            t = self._total
        for i in range(len(self._pts) - 1):
            if t <= self._cum[i + 1] or i == len(self._pts) - 2:
                seg = self._seglens[i]
                a, b = self._pts[i], self._pts[i + 1]
                if seg <= 0.0:
                    return Point3d(b)
                f = (t - self._cum[i]) / seg
                return Point3d(a.X + f * (b.X - a.X),
                               a.Y + f * (b.Y - a.Y),
                               a.Z + f * (b.Z - a.Z))
        return Point3d(self._pts[-1])

    def TangentAt(self, t):
        if self._total <= 0.0 or len(self._pts) < 2:
            return Vector3d(1, 0, 0)
        if t < 0.0:
            t = 0.0
        if t > self._total:
            t = self._total
        for i in range(len(self._pts) - 1):
            if t <= self._cum[i + 1] or i == len(self._pts) - 2:
                a, b = self._pts[i], self._pts[i + 1]
                dx = b.X - a.X
                dy = b.Y - a.Y
                L = math.sqrt(dx * dx + dy * dy)
                if L < 1e-12:
                    return Vector3d(1, 0, 0)
                return Vector3d(dx / L, dy / L, 0.0)
        a, b = self._pts[-2], self._pts[-1]
        return Vector3d(b.X - a.X, b.Y - a.Y, 0)

    def ToPolyline(self, tol=0.0):
        pl = Polyline()
        for p in self._pts:
            pl.Add(p)
        return pl

    def TryGetPolyline(self):
        return (True, self.ToPolyline())

    def ToNurbsCurve(self):
        return self

    def DuplicateCurve(self):
        return PolylineCurve(self)

    def Translate(self, v):
        for p in self._pts:
            p.X += v.X
            p.Y += v.Y
            p.Z += v.Z
        return True

    def GetBoundingBox(self, exact=False):
        xs = [p.X for p in self._pts]
        ys = [p.Y for p in self._pts]
        zs = [p.Z for p in self._pts]
        bb = type('BBox', (object,), {})()
        bb.Min = Point3d(min(xs), min(ys), min(zs))
        bb.Max = Point3d(max(xs), max(ys), max(zs))
        return bb

    @property
    def IsClosed(self):
        if len(self._pts) < 2:
            return False
        return self._pts[0].DistanceTo(self._pts[-1]) < 1e-8

    @property
    def IsValid(self):
        return True


class Curve(object):
    @staticmethod
    def CreateBooleanDifference(curve, cutters, tol):
        # Minimal stub: if cutters exist, return empty list (simulates difference)
        return []

    @staticmethod
    def CreateBooleanUnion(curves, tol):
        return None

    @staticmethod
    def CreatePlanarBreps(curves, tol):
        # Delegate to Brep.CreatePlanarBreps
        return Brep.CreatePlanarBreps(curves, tol)

    def TryGetPolyline(self):
        if hasattr(self, '_pts'):
            return (True, self.ToPolyline())
        return (False, None)

    def IsClosed(self):
        return getattr(self, '_closed', False)

    def IsValid(self):
        return True


class Line(object):
    def __init__(self, a, b):
        self.From = Point3d(a)
        self.To = Point3d(b)


# ---------------- intersecciones ----------------

def _seg_seg(a1, a2, b1, b2):
    d1x = a2.X - a1.X
    d1y = a2.Y - a1.Y
    d2x = b2.X - b1.X
    d2y = b2.Y - b1.Y
    den = d1x * d2y - d1y * d2x
    if abs(den) < 1e-12:
        return None
    t = ((b1.X - a1.X) * d2y - (b1.Y - a1.Y) * d2x) / den
    u = ((b1.X - a1.X) * d1y - (b1.Y - a1.Y) * d1x) / den
    if -1e-9 <= t <= 1.0 + 1e-9 and -1e-9 <= u <= 1.0 + 1e-9:
        return Point3d(a1.X + t * d1x, a1.Y + t * d1y, 0.0)
    return None


class IntersectionEvent(object):
    def __init__(self, p):
        self.PointA = p
        self.PointB = p
        self.IntersectionType = 'Point'


class EventList(list):
    @property
    def Count(self):
        return len(self)


class Intersection(object):
    Point = 'Point'
    Overlap = 'Overlap'

    @staticmethod
    def CurveCurve(c1, c2, t1=0.0, t2=0.0):
        ev = EventList()
        for i in range(len(c1._pts) - 1):
            for j in range(len(c2._pts) - 1):
                p = _seg_seg(c1._pts[i], c1._pts[i + 1], c2._pts[j], c2._pts[j + 1])
                if p is not None:
                    ev.append(IntersectionEvent(p))
        return ev

    @staticmethod
    def CurveLine(c, line, t1=0.0, t2=0.0):
        ev = EventList()
        for i in range(len(c._pts) - 1):
            p = _seg_seg(c._pts[i], c._pts[i + 1], line.From, line.To)
            if p is not None:
                ev.append(IntersectionEvent(p))
        return ev


class _IntersectNS(object):
    Intersection = Intersection


# ---------------- modulo Rhino.Geometry ----------------
Intersect = _IntersectNS

class AreaMassProperties(object):
    @staticmethod
    def Compute(obj):
        # obj can be PolylineCurve or Brep
        if hasattr(obj, '_pts'):
            # PolylineCurve -> area via shoelace
            pts = obj._pts
            if len(pts) < 3:
                return None
            area = 0.0
            n = len(pts)
            for i in range(n):
                p1 = pts[i]
                p2 = pts[(i + 1) % n]
                area += p1.X * p2.Y - p2.X * p1.Y
            area = abs(area) / 2.0
            cx = sum(p.X for p in pts) / float(n)
            cy = sum(p.Y for p in pts) / float(n)
            cz = sum(p.Z for p in pts) / float(n)
            class Props:
                Area = area
                Centroid = Point3d(cx, cy, cz)
            return Props()
        elif hasattr(obj, '_breps'):
            # Brep list
            total = 0.0
            for b in obj._breps:
                total += b.Area
            class Props:
                Area = total
            return Props()
        return None


class Brep(object):
    def __init__(self, curves):
        self._curves = curves
        # compute area from first curve
        if curves:
            c = curves[0]
            if hasattr(c, '_pts'):
                pts = c._pts
                area = 0.0
                n = len(pts)
                for i in range(n):
                    p1 = pts[i]
                    p2 = pts[(i + 1) % n]
                    area += p1.X * p2.Y - p2.X * p1.Y
                self.Area = abs(area) / 2.0
            else:
                self.Area = 0.0
        else:
            self.Area = 0.0

    @staticmethod
    def CreatePlanarBreps(curves, tol):
        if not curves:
            return None
        if not isinstance(curves, (list, tuple)):
            curves = [curves]
        # Wrap each curve in a Brep
        breps = []
        for c in curves:
            breps.append(Brep([c]))
        return breps


__all__ = ['Point3d', 'Vector3d', 'Polyline', 'PolylineCurve', 'Line',
           'Intersection', 'IntersectionEvent', 'EventList', 'Intersect',
           'AreaMassProperties', 'Brep', 'Curve']
