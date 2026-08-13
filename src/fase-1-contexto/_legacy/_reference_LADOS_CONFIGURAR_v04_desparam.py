import json
import rhinoscriptsyntax as rs

# 1. Inicializar todas las salidas al inicio para evitar <null>
pot_compilance = json.dumps({'status': 'init_error'})
sides_table = json.dumps([])
setbacks_matrix = json.dumps({})
balcony_rules_summary = json.dumps({})

try:
    # 2. Saneamiento extremo de pot_conclusions
    pot_data = {}
    pot_status = 'no_data'
    
    if pot_conclusions:
        pot_text = ""
        if isinstance(pot_conclusions, (list, tuple)):
            pot_text = "".join([str(item) for item in pot_conclusions if item is not None])
        else:
            pot_text = str(pot_conclusions)
            
        if pot_text.strip() not in ["", "<null>"]:
            try:
                pot_data = json.loads(pot_text)
                pot_status = 'ok'
            except Exception as json_err:
                pot_status = 'json_parse_error'
        else:
            pot_status = 'empty_input'
    else:
        pot_status = 'no_data'
        
    pot_compilance = json.dumps({'status': pot_status})
    
    # 3. Extraer retrocesos del POT (Valores reales o Fallback por defecto)
    front_setback = 3.0
    side_setback = 3.0
    rear_setback = 3.0
    road_class = "DESCONOCIDA"
    
    if pot_status == 'ok' and 'road_analysis' in pot_data:
        road_analysis = pot_data['road_analysis']
        if isinstance(road_analysis, list) and len(road_analysis) > 0:
            # Tomar la primera vía detectada como referencia principal
            first_road = road_analysis[0]
            road_class = first_road.get('classification', 'DESCONOCIDA')
            
            if 'setbacks' in first_road:
                setbacks = first_road['setbacks']
                front_setback = setbacks.get('front', 3.0)
                side_setback = setbacks.get('side', 3.0)
                rear_setback = setbacks.get('rear', 3.0)

    # 4. Procesar los lados del lote
    sides = []
    if isinstance(lot_segments, list):
        for i, seg in enumerate(lot_segments):
            sides.append({
                'index': i,
                'pot_status': pot_status,
                'road_class': road_class,
                'setback_m': front_setback,  # Nombrado así para compatibilidad con ANALISIS_VECINOS
                'side_setback_m': side_setback,
                'rear_setback_m': rear_setback
            })
    else:
        # Si no es lista, al menos crea un lado para que no colapse el siguiente script
        sides.append({
            'index': 0, 
            'pot_status': pot_status, 
            'setback_m': front_setback,
            'note': 'Set List Access on lot_segments!'
        })
        
    sides_table = json.dumps(sides)
    
    # 5. Generar matrices de resumen
    setbacks_matrix = json.dumps({
        'front': front_setback,
        'side': side_setback,
        'rear': rear_setback,
        'source': 'POT_EXTRACTED' if pot_status == 'ok' else 'DEFAULT_FALLBACK'
    })
    
    # Resumen de balcones (si existe en el POT)
    balcony_data = {}
    if pot_status == 'ok' and 'balcony_rules' in pot_data:
        balcony_data = pot_data['balcony_rules']
    balcony_rules_summary = json.dumps({
        'status': 'ok', 
        'rules': balcony_data if balcony_data else 'No aplicable o sin datos'
    })
    
except Exception as e:
    print("ERROR FATAL EN CONFIGURAR_LADOS: " + str(e))
    pot_compilance = json.dumps({'status': 'fatal_error', 'error': str(e)})
    # En caso de error fatal, igual entregar un sides_table básico
    sides_table = json.dumps([{'index': 0, 'setback_m': 3.0, 'error': str(e)}])