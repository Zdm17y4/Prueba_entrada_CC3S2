def summarize(nums):

    if not nums:
        raise ValueError("La lista no puede estar vacía")
    
    try:
        # Convertir a float y validar
        numbers = []
        for item in nums:
            try:
                num = float(item)
                numbers.append(num)
            except (ValueError, TypeError):
                raise ValueError(f"Elemento no numérico: {item}")
        
        count = len(numbers)
        total_sum = sum(numbers)
        average = total_sum / count if count > 0 else 0
        
        return {
            "count": count,
            "sum": total_sum,
            "avg": average
        }
    
    except Exception as e:
        raise ValueError(f"Error procesando números: {e}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Uso: python3 -m app \"1,2,3\"")
        sys.exit(1)
    
    try:
        raw = sys.argv[1]
        items = [p.strip() for p in raw.split(",") if p.strip()]
        
        result = summarize(items)
        
        #Formato solicitado
        print(f"sum={result['sum']} avg={result['avg']} count={result['count']}")
        
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    except Exception as e:
        print(f"Error inesperado: {e}")
        sys.exit(1)