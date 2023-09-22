import requests



class FlightService:

    @staticmethod
    def get_external_airports(url):
        try:
            response = requests.get(url)

            if response.status_code != 200:
                return []
            return response.json()
        
        except Exception:
            raise Exception("Error could not retreive airports")
        


