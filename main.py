import data
from helpers import is_url_reachable # Importa o módulo helpers para verificar conectividade


class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        if is_url_reachable(data.URBAN_ROUTES_URL): # Verifica se o servidor UrbanRoutes está acessível
            print("Conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução.")

    def test_set_route(self):
        # Adicionar S8
        pass

    def test_select_plan(self):
        # Adicionar S8
        pass

    def test_fill_phone_number(self):
        # Adicionar S8
        pass

    def test_fill_card(self):
        # Adicionar S8
        pass

    def test_comment_for_driver(self):
        # Adicionar S8
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Adicionar S8
        pass

    def test_order_2_ice_creams(self):
        # Adicionar S8
        print("Função para adicionar dois sorvetes")
        for i in range(2): # Loop para adicionar 2 sorvetes ao pedido
            #Adicionar em S8
            pass

    def test_car_search_model_appears(self):
        # Adicionar S8
        pass


