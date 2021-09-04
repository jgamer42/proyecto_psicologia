from googlesearch import search
import urllib
def buscar(pagina):
    site = f"https://www.{pagina}.com/politica/"
    palabra = "acuerdos de paz"
    query = f"site:{site} {palabra} after:2015"
    salida = []
    try:
        data = search(query,tld="com",lang="es",pause=10.0,stop=None)
        for i in data:
            salida.append(i)
            #print(i)
    except(urllib.error.HTTPError):
        print("error de request")
    except:
        print("otro")
    finally:
        return salida