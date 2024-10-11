from botcity.core import DesktopBot

class Bot(DesktopBot):
        def action(self, execution=None):

            #######################-----LOGIN-----############################
        
            #self.execute(r"C:\Users\Rafael\Desktop\2207\faturamento.exe")
            self.execute(r"C:\Users\Rafael\Desktop\2207\teste23\23mes07\faturamento.exe")
            
            if not self.find( "btn_codigo_usuario", matching=0.97, waiting_time=100000):
                self.not_found("btn_codigo_usuario")
            self.click_relative(47, 12)
                    
            self.type_keys_with_interval(1,"999")
            self.wait(500)
            self.type_keys_with_interval(1,"tsfmx24")
            self.enter()

            if not self.find( "btn_login", matching=0.97, waiting_time=10000):
                self.not_found("btn_login")
            self.click()
            self.enter()

            ###################################################################

            self.wait(1500)
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            #self.type_down()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_estoque", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_estoque")
            self.click()
            if not self.find( "r_posAtualEstoque", matching=0.97, waiting_time=10000):
                self.not_found("r_posAtualEstoque")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            x=0
            while x<6:
                self.type_right()
                x=x+1
            self.tab()
            self.type_right()
            self.tab()
            self.type_right()
            self.type_right()
            self.type_right()
            self.tab()
            if not self.find( "b_grupoEmpresa_r_posEstoque", matching=0.97, waiting_time=10000):
                self.not_found("b_grupoEmpresa_r_posEstoque")
            self.click_relative(63, 211)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            self.tab()
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            self.tab()
            x=0
            while x<3:
                self.type_right()
                self.tab()
                x=x+1
            self.type_right()
            self.type_right()
            self.tab()
            x=0
            while x<8:
                self.type_right()
                x=x+1
            self.tab()
            x=0
            while x<4:
                self.space()
                self.space()
                self.tab()
                x=x+1
            x=0
            while x<10:
                self.type_right()
                x=x+1
            self.tab()
            x=0
            while x<6:
                self.type_right()
                x=x+1
            self.tab()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R POSICAO ESTOQUE PEDIDO COMPRA---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            self.type_down()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_estoque", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_estoque")
            self.click()
            if not self.find( "r_posEstoquePedCompra", matching=0.97, waiting_time=10000):
                self.not_found("r_posEstoquePedCompra")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            x=0
            while x<6:
                self.type_right()
                x=x+1
            self.tab()
            self.type_right()
            self.tab()
            self.type_right()
            self.type_right()
            self.type_right()
            self.tab()
            if not self.find( "b_grupoEmpresa_posEstoquePed", matching=0.97, waiting_time=10000):
                self.not_found("b_grupoEmpresa_posEstoquePed")
            self.click_relative(63, 197)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            self.tab()
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            self.tab()
            x=0
            while x<3:
                self.type_right()
                self.tab()
                x=x+1
            self.type_right()
            self.type_right()
            self.tab()
            x=0
            while x<8:
                self.type_right()
                x=x+1
            self.tab()
            x=0
            while x<4:
                self.space()
                self.space()
                self.tab()
                x=x+1
            x=0
            while x<10:
                self.type_right()
                x=x+1
            self.tab()
            x=0
            while x<6:
                self.type_right()
                x=x+1
            self.tab()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R ESTOQUE ACIMA MAXIMO ABAIXO MIN---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            self.type_down()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_estoque", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_estoque")
            self.click()
            if not self.find( "r_estoqueAcimaMax", matching=0.97, waiting_time=10000):
                self.not_found("r_estoqueAcimaMax")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            self.type_right()
            self.type_right()
            self.type_right()
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            x=0
            while x<2:
                self.space()
                self.space()
                self.tab()
                x=x+1
            self.type_right()
            self.tab()
            self.type_right()
            self.type_right()
            self.type_right()
            self.type_right()
            self.tab()
            x=0
            while x<3:
                self.type_right()
                x=x+1
            self.tab()
            x=0
            while x<3:
                self.type_right()
                x=x+1
            self.tab()
            self.type_keys_with_interval(1,'123')
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R ESTOQUE NEGATIVO OU ZERADO---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            self.type_down()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_estoque", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_estoque")
            self.click()
            if not self.find( "r_estoqueNegativoZerado", matching=0.97, waiting_time=10000):
                self.not_found("r_estoqueNegativoZerado")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            x=0
            while x<6:
                self.type_right()
                x=x+1
            self.tab()
            self.type_right()
            self.tab()
            self.type_right()
            self.type_right()
            self.type_right()
            self.tab()
            if not self.find( "b_grupoEmpresa_r_posEstoque", matching=0.97, waiting_time=10000):
                self.not_found("b_grupoEmpresa_r_posEstoque")
            self.click_relative(63, 211)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            self.tab()
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            self.tab()
            x=0
            while x<3:
                self.type_right()
                self.tab()
                x=x+1
            self.type_right()
            self.type_right()
            self.tab()
            x=0
            while x<8:
                self.type_right()
                x=x+1
            self.tab()
            x=0
            while x<4:
                self.space()
                self.space()
                self.tab()
                x=x+1
            x=0
            while x<10:
                self.type_right()
                x=x+1
            self.tab()
            x=0
            while x<6:
                self.type_right()
                x=x+1
            self.tab()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R POSICAO ESTOQUE---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            self.type_down()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_estoque", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_estoque")
            self.click()
            if not self.find( "r_posicaoEstoque", matching=0.97, waiting_time=10000):
                self.not_found("r_posicaoEstoque")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            x=0
            while x<4:
                self.type_right()
                self.type_right()
                self.type_right()
                self.tab()
                x=x+1
            x=0
            while x<6:
                self.type_right()
                x=x+1
            self.tab()
            self.type_right()
            self.type_right()
            self.type_right()
            self.tab()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R ESTOQUE PRODUTOS TRANSFERIR---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            self.type_down()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_estoque", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_estoque")
            self.click()
            if not self.find( "r_estoqueProdutosTransferir", matching=0.97, waiting_time=10000):
                self.not_found("r_estoqueProdutosTransferir")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            self.type_right()
            self.type_right()
            self.type_right()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R ITENS DATA VENCIMENTO---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            self.type_down()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_estoque", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_estoque")
            self.click()
            if not self.find( "r_itensLotesDataVencimento", matching=0.97, waiting_time=10000):
                self.not_found("r_itensLotesDataVencimento")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            if not self.find( "b_grupoEmpresa_r_ItensLotesDataVencimento", matching=0.97, waiting_time=10000):
                self.not_found("b_grupoEmpresa_r_ItensLotesDataVencimento")
            self.click_relative(120, 128)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            self.tab()
            self.tab()
            self.type_down()
            x=0
            while x<5:
                self.type_up()
                x=x+1
            self.tab()
            x=0
            while x<2:
                self.type_down()
                x=x+1
            self.tab()
            x=0
            while x<2:
                self.type_down()
                x=x+1
            self.tab()
            x=0
            while x<3:
                self.type_down()
                x=x+1
            self.tab()
            x=0
            while x<3:
                self.type_down()
                x=x+1
            self.tab()
            self.type_keys_with_interval(1,'123')
            if not self.find( "info_r_itensLotesDataVencimento2", matching=0.97, waiting_time=10000):
                self.not_found("info_r_itensLotesDataVencimento2")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R VARIACOES DE ESTOQUE---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            self.type_down()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_estoque", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_estoque")
            self.click()
            if not self.find( "r_variacoesEstoque", matching=0.97, waiting_time=10000):
                self.not_found("r_variacoesEstoque")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.tab()
            x=0
            while x<2:
                self.type_right()
                self.type_right()
                self.type_right()
                self.tab()
                x=x+1
            x=0
            while x<5:
                self.type_right()
                x=x+1
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R ESTOQUE RESERVADO---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            self.type_down()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_estoque", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_estoque")
            self.click()
            if not self.find( "r_estoqueReservado", matching=0.97, waiting_time=10000):
                self.not_found("r_estoqueReservado")
            self.click()
            x=0
            while x<8:
                self.type_right()
                x=x+1
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R LISTA DE PRECOS---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            self.type_down()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_relacoes", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_relacoes")
            self.click()
            if not self.find( "r_listaPrecos", matching=0.97, waiting_time=10000):
                self.not_found("r_listaPrecos")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.tab()
            x=0
            while x<4:
                self.space()
                self.space()
                self.tab()
                x=x+1
            self.type_right()
            self.type_right()
            self.tab()
            x=0
            while x<4:
                self.type_right()
                x=x+1
            self.tab()
            x=0
            while x<7:
                self.type_right()
                x=x+1
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            self.type_right()
            self.type_right()
            self.type_right()
            self.tab()
            self.type_right()
            self.type_right()
            self.type_right()
            self.type_right()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            if not self.find( "op_custo1_r_listaPreco", matching=0.97, waiting_time=10000):
                self.not_found("op_custo1_r_listaPreco")
            self.click_relative(16, 248)
            x=0
            while x<5:
                self.type_right()
                x=x+1
            self.tab()
            x=0
            while x<5:
                self.type_right()
                x=x+1
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R LISTA PRECO TABELA---####
            
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            self.type_down()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_relacoes", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_relacoes")
            self.click()
            if not self.find( "r_listaPrecoTabela", matching=0.97, waiting_time=10000):
                self.not_found("r_listaPrecoTabela")
            self.click()
            self.type_right()
            self.type_right()
            self.tab()
            self.tab()
            x=0
            while x<4:
                self.type_right()
                x=x+1
            self.tab()
            x=0
            while x<3:
                self.type_right()
                x=x+1
            self.tab()
            self.type_right()
            self.type_right()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R LISTA PRECO FORNECEDOR---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            self.type_down()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_relacoes", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_relacoes")
            self.click()
            if not self.find( "r_listaPrecoFornecedor", matching=0.97, waiting_time=10000):
                self.not_found("r_listaPrecoFornecedor")
            self.click()
            self.type_right()
            self.type_right()
            self.tab()
            self.tab()
            x=0
            while x<4:
                self.type_right()
                x=x+1
            self.tab()
            x=0
            while x<3:
                self.type_right()
                x=x+1
            self.tab()
            self.type_right()
            self.type_right()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R LISTA PRECO ITENS TABELAS---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            self.type_down()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_relacoes", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_relacoes")
            self.click()
            if not self.find( "r_listaPrecosItensTabelas", matching=0.97, waiting_time=10000):
                self.not_found("r_listaPrecosItensTabelas")
            self.click()
            x=0
            while x<2:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.type_right()
            self.tab()
            x=0
            while x<4:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R PRECOS ALTERADOS PERIODO---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            self.type_down()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_relacoes", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_relacoes")
            self.click()
            if not self.find( "r_precosAlteradosPeriodo", matching=0.97, waiting_time=10000):
                self.not_found("r_precosAlteradosPeriodo")
            self.click()
            x=0
            while x<2:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.type_right()
            self.tab()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R ITENS EM OFERTA---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            self.type_down()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_relacoes", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_relacoes")
            self.click()
            if not self.find( "r_itensEmOferta", matching=0.97, waiting_time=10000):
                self.not_found("r_itensEmOferta")
            self.click()
            x=0
            while x<3:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            x=0
            while x<6:
                self.type_right()
                x=x+1
            self.tab()
            x=0
            while x<5:
                self.type_right()
                x=x+1
            self.tab()
            x=0
            while x<3:
                self.type_right()
                x=x+1
            self.tab()
            x=0
            while x<4:
                self.type_right()
                x=x+1
            self.tab()
            self.type_right()
            self.tab()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R FISICO FINANCEIRO---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            self.type_down()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_relacoes", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_relacoes")
            self.click()
            if not self.find( "r_fisicoFinanceiro", matching=0.97, waiting_time=10000):
                self.not_found("r_fisicoFinanceiro")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            x=0
            while x<5:
                self.type_right()
                x=x+1
            self.tab()
            x=0
            while x<2:
                self.type_right()
                x=x+1
            self.tab()
            self.tab()
            x=0
            while x<2:
                self.type_right()
                x=x+1
            self.tab()
            x=0
            while x<2:
                self.space()
                self.space()
                x=x+1
            self.tab()
            x=0
            while x<2:
                self.type_right()
                x=x+1
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            x=0
            while x<4:
                self.type_right()
                x=x+1
            self.tab()
            self.space()
            self.space()
            self.tab()
            x=0
            while x<5:
                self.type_right()
                x=x+1
            self.tab()
            x=0
            while x<3:
                self.type_right()
                x=x+1
            self.tab()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R COMPOSICAO ITENS---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            self.type_down()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_relacoes", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_relacoes")
            self.click()
            if not self.find( "r_composicaoItens", matching=0.97, waiting_time=10000):
                self.not_found("r_composicaoItens")
            self.click()
            self.type_right()
            self.type_right()
            self.tab()
            x=0
            while x<2:
                self.space()
                self.space()
                self.tab()
                x=x+1
            self.tab()
            self.type_right()
            self.type_right()
            self.type_right()
            self.tab()
            if not self.find( "b_item_r_composicaoItem", matching=0.97, waiting_time=10000):
                self.not_found("b_item_r_composicaoItem")
            self.click_relative(590, 82)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.tab()
            self.tab()
            x=0
            while x<3:
                self.type_right()
                x=x+1
            self.tab()
            if not self.find( "op_selecioneCusto_r_compItens", matching=0.97, waiting_time=10000):
                self.not_found("op_selecioneCusto_r_compItens")
            self.click_relative(260, 94)
            x=0
            while x<3:
                self.type_right()
                x=x+1
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R ALOCACAO MATERIA PRIMA---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            self.type_down()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_relacoes", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_relacoes")
            self.click()
            if not self.find( "r_alocacaoMateriaPrima", matching=0.97, waiting_time=10000):
                self.not_found("r_alocacaoMateriaPrima")
            self.click()
            self.type_right()
            self.type_right()
            self.tab()
            self.type_keys_with_interval(1,'123')
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R EMBALAGENS DE DEFENSIVOS---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            self.type_down()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_relacoes", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_relacoes")
            self.click()
            if not self.find( "r_embalagensDefensivos", matching=0.97, waiting_time=10000):
                self.not_found("r_embalagensDefensivos")
            self.click()
            x=0
            while x<4:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()

                            ####---R PEDIDOS ORÇAMENTO ETC---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            self.type_down()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_vendas", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_vendas")
            self.click()
            if not self.find( "r_pedidosOrcamentoVendas", matching=0.97, waiting_time=10000):
                self.not_found("r_pedidosOrcamentoVendas")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.tab()
            x=0
            while x<5:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            x=0
            while x<7:
                self.type_right()
                x=x+1
            self.tab()
            self.space()
            x=0
            while x<15:
                self.space()
                self.type_down()
                x=x+1
            self.tab()
            x=0
            while x<5:
                self.type_right()
                x=x+1
            x=0
            while x<4:
                self.tab()
                x=x+1
            self.type_right()
            self.tab()
            self.tab()
            x=0
            while x<5:
                self.type_right()
                x=x+1
            self.tab()
            x=0
            while x<9:
                self.space()
                self.tab()
                x=x+1
            x=0
            while x<4:
                self.type_right()
                x=x+1
            self.tab()
            x=0
            while x<4:
                self.type_right()
                x=x+1
            self.tab()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R PEDIDOS VENDA POR CONDICAO---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            self.type_down()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_vendas", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_vendas")
            self.click()
            if not self.find( "r_vendasCondicao", matching=0.97, waiting_time=10000):
                self.not_found("r_vendasCondicao")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            self.tab()
            self.type_right()
            self.tab()
            x=0
            while x<12:
                self.type_right()
                x=x+1
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R PEDIDOS VENDA FATURADO---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            self.type_down()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_vendas", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_vendas")
            self.click()
            if not self.find( "r_pedidosFaturados", matching=0.97, waiting_time=10000):
                self.not_found("r_pedidosFaturados")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R PEDIDOS VENDA ITENS A PRODUZIR---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_vendas", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_vendas")
            self.click()
            if not self.find( "r_pedidosVendaProduzir", matching=0.97, waiting_time=10000):
                self.not_found("r_pedidosVendaProduzir")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.type_right()
            self.type_right()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R VENDA MEDIA DIAS---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_vendas", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_vendas")
            self.click()
            if not self.find( "r_pedidosVendaMediaDias", matching=0.97, waiting_time=10000):
                self.not_found("r_pedidosVendaMediaDias")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.type_right()
            self.type_right()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.space()
            self.space()
            self.tab()
            self.tab()
            self.type_right()
            self.tab()
            x=0
            while x<10:
                self.type_right()
                x=x+1
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R PEDIDO VENDA DEMONSTRATIVO---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_vendas", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_vendas")
            self.click()
            if not self.find( "r_pedidoVendaDemonstrativo", matching=0.97, waiting_time=10000):
                self.not_found("r_pedidoVendaDemonstrativo")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            x=0
            while x<11:
                self.type_right()
                x=x+1
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R VENDAS E DEVOLUCOES CONDICIONAIS---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_vendas", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_vendas")
            self.click()
            if not self.find( "r_vendasDevolucoesCondicionais", matching=0.97, waiting_time=10000):
                self.not_found("r_vendasDevolucoesCondicionais")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R RELACAO NOTAS FISCAIS---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_vendas", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_vendas")
            self.click()
            if not self.find( "r_notasFiscais", matching=0.97, waiting_time=10000):
                self.not_found("r_notasFiscais")
            self.click()
            if not self.find( "r_relacaoNotasFiscais", matching=0.97, waiting_time=10000):
                self.not_found("r_relacaoNotasFiscais")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            x=0
            while x<8:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            x=0
            while x<7:
                self.space()
                self.space()
                self.tab()
                x=x+1
            self.tab()
            self.type_right()
            self.tab()
            self.type_right()
            self.tab()
            self.space()
            self.space()
            self.tab()
            self.space()
            self.space()
            self.tab()
            self.type_right()
            self.tab()
            x=0
            while x<5:
                self.type_right()
                x=x+1
            self.tab()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R ITENS DE NFS---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_vendas", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_vendas")
            self.click()
            if not self.find( "r_notasFiscais", matching=0.97, waiting_time=10000):
                self.not_found("r_notasFiscais")
            self.click()
            if not self.find( "r_itensDeNFs", matching=0.97, waiting_time=10000):
                self.not_found("r_itensDeNFs")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            x=0
            while x<2:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.tab()
            self.tab()
            self.tab()
            self.type_left()
            self.type_left()
            if not self.find( "op_SitNF_r_NFitensAgrupados", matching=0.97, waiting_time=10000):
                self.not_found("op_SitNF_r_NFitensAgrupados")
            self.click_relative(18, 124)           
            self.type_right()
            self.type_right()
            if not self.find( "op_tipoImpressao_r_NFitens", matching=0.97, waiting_time=10000):
                self.not_found("op_tipoImpressao_r_NFitens")
            self.click_relative(293, 134)
            self.type_right()
            if not self.find( "op_agruparPor_r_NFitens", matching=0.97, waiting_time=10000):
                self.not_found("op_agruparPor_r_NFitens")
            self.click_relative(477, 125)
            self.type_right()
            self.type_right()
            self.type_right()
            self.type_right()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R RELACAO NF COM SITUACAO---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_vendas", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_vendas")
            self.click()
            if not self.find( "r_notasFiscais", matching=0.97, waiting_time=10000):
                self.not_found("r_notasFiscais")
            self.click()
            if not self.find( "r_relacaoNFComSituacao", matching=0.97, waiting_time=10000):
                self.not_found("r_relacaoNFComSituacao")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            if not self.find( "op_periodo_r_NFexp", matching=0.97, waiting_time=10000):
                self.not_found("op_periodo_r_NFexp")
            self.click_relative(460, 84)
            self.type_right()
            self.type_right()
            self.type_right()
            if not self.find( "op_relacionarNF_r_NFexp", matching=0.97, waiting_time=10000):
                self.not_found("op_relacionarNF_r_NFexp")
            self.click_relative(15, 142)
            self.type_right()
            self.type_right()
            if not self.find( "op_situacaoNF_r_NFexp", matching=0.97, waiting_time=10000):
                self.not_found("op_situacaoNF_r_NFexp")
            self.click_relative(467, 143)
            self.type_right()
            self.type_right()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R RELACAO NF COM CALCULO---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_vendas", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_vendas")
            self.click()
            if not self.find( "r_notasFiscais", matching=0.97, waiting_time=10000):
                self.not_found("r_notasFiscais")
            self.click()
            if not self.find( "r_relacaoNFcomCalculo", matching=0.97, waiting_time=10000):
                self.not_found("r_relacaoNFcomCalculo")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R RELACAO NF POR ITEM---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_vendas", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_vendas")
            self.click()
            if not self.find( "r_notasFiscais", matching=0.97, waiting_time=10000):
                self.not_found("r_notasFiscais")
            self.click()
            if not self.find( "r_NFporItens", matching=0.97, waiting_time=10000):
                self.not_found("r_NFporItens")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            x=0
            while x<5:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.tab()
            self.type_right()
            self.tab()
            self.space()
            self.space()
            self.tab()
            self.space()
            self.space()
            self.tab()
            self.type_right()
            self.tab()
            self.type_right()
            self.tab()
            self.space()
            self.space()
            self.tab()
            if not self.find( "op_relacaoNF_r_NFitens", matching=0.97, waiting_time=10000):
                self.not_found("op_relacaoNF_r_NFitens")
            self.click_relative(15, 130)
            self.type_right()
            self.type_right()
            if not self.find( "op_sitNF_r_NFitens", matching=0.97, waiting_time=10000):
                self.not_found("op_sitNF_r_NFitens")
            self.click_relative(318, 127)
            self.type_right()
            self.type_right()
            self.type_right()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R CARTAS DE CORRECAO---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_vendas", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_vendas")
            self.click()
            if not self.find( "r_notasFiscais", matching=0.97, waiting_time=10000):
                self.not_found("r_notasFiscais")
            self.click()
            if not self.find( "r_cartasDeCorrecao", matching=0.97, waiting_time=10000):
                self.not_found("r_cartasDeCorrecao")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'123')
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R ITENS A ENTREGAR---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_vendas", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_vendas")
            self.click()
            if not self.find( "r_mov_relacaoEntregas", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_relacaoEntregas")
            self.click()
            if not self.find( "r_relacaoItensAEntregar", matching=0.97, waiting_time=10000):
                self.not_found("r_relacaoItensAEntregar")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.tab()
            self.type_right()
            self.type_right()
            self.type_right()
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            self.type_right()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R DEMONSTRATIVO DOCUMENTOS UTILIZADOS---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_vendas", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_vendas")
            self.click()
            if not self.find( "r_demonstrativoDocumentos", matching=0.97, waiting_time=10000):
                self.not_found("r_demonstrativoDocumentos")
            self.click()
            x=0
            while x<6:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R ORDENS DE SERVICO---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_vendas", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_vendas")
            self.click()
            if not self.find( "r_ordensDeServico", matching=0.97, waiting_time=10000):
                self.not_found("r_ordensDeServico")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            x=0
            while x<3:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.tab()
            self.tab()
            self.tab()
            x=0
            while x<6:
                self.type_right()
                x=x+1
            self.tab()
            x=0
            while x<12:
                self.space()
                self.tab()
                x=x+1
            self.type_right()
            self.type_right()
            self.tab()
            self.type_right()
            self.type_right()
            self.type_right()
            self.type_right()
            self.tab()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R RATEIO DE SERVICOS---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_vendas", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_vendas")
            self.click()
            if not self.find( "r_rateioDeServicos", matching=0.97, waiting_time=10000):
                self.not_found("r_rateioDeServicos")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            x=0
            while x<5:
                self.type_right()
                x=x+1
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            self.type_right()
            self.tab()
            self.type_right()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R RELATORIO DE ALOCACOES---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_vendas", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_vendas")
            self.click()
            if not self.find( "r_relatorioAlocacoes", matching=0.97, waiting_time=10000):
                self.not_found("r_relatorioAlocacoes")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            x=0
            while x<5:
                self.type_right()
                x=x+1
            self.tab()
            self.type_right()
            self.tab()
            self.space()
            self.space()
            self.tab()
            self.space()
            self.space()           
            if not self.find( "filtro_claro", matching=0.97, waiting_time=10000):
                self.not_found("filtro_claro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retirar_mouse", matching=0.97, waiting_time=10000):
                self.not_found("retirar_mouse")
            self.click() 
            if not self.find( "informacoes_claro_alocacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes_claro_alocacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "retornar_claro_alocacoes", matching=0.97, waiting_time=10000):
                self.not_found("retornar_claro_alocacoes")
            self.click()
            
                            ####---R ORDEM DE SERVICO RATEADO---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_vendas", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_vendas")
            self.click()
            if not self.find( "r_ordemDeServicoRateado", matching=0.97, waiting_time=10000):
                self.not_found("r_ordemDeServicoRateado")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.tab()
            self.type_right()
            self.tab()
            self.type_right()
            self.tab()
            self.type_right()
            self.tab()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R MAPA DE VENDAS---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_vendas", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_vendas")
            self.click()
            if not self.find( "r_mapaDeVendas", matching=0.97, waiting_time=10000):
                self.not_found("r_mapaDeVendas")
            self.click()
            self.tab()
            x=0
            while x<8:
                self.space()
                self.tab()
                x=x+1
            self.tab()
            self.tab()
            self.tab()
            x=0
            while x<4:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.type_right()
            self.tab()
            self.type_right()
            self.tab()
            x=0
            while x<15:
                self.type_down()
                x=x+1
            self.tab()
            self.type_right()
            self.tab()
            self.type_right()
            self.type_right()
            self.type_right()
            self.tab()
            x=0
            while x<7:
                self.type_right()
                x=x+1
            self.tab()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()

                            ####---R VENDAS PERDIDAS---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_vendas", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_vendas")
            self.click()
            if not self.find( "r_vendasPerdidas", matching=0.97, waiting_time=10000):
                self.not_found("r_vendasPerdidas")
            self.click()
            x=0
            while x<3:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.type_right()
            self.tab()
            x=0
            while x<4:
                self.type_right()
                x=x+1
            self.tab()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()

                            ####---R VENDAS E SERVICO DIARIO---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_vendas", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_vendas")
            self.click()
            if not self.find( "r_vendasServicoDiario", matching=0.97, waiting_time=10000):
                self.not_found("r_vendasServicoDiario")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            self.space()
            self.space()
            self.tab()
            self.space()
            self.space()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R VENDAS POR VENDEDORES---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_vendas", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_vendas")
            self.click()
            if not self.find( "r_vendasPorVendedores", matching=0.97, waiting_time=10000):
                self.not_found("r_vendasPorVendedores")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()

                            ####---R VENDAS POR CAIXA---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_vendas", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_vendas")
            self.click()
            if not self.find( "r_vendasPorCaixa", matching=0.97, waiting_time=10000):
                self.not_found("r_vendasPorCaixa")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            x=0
            while x<3:
                self.space()
                self.space()
                self.tab()
                x=x+1
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()

                            ####---R VENDAS CAIXA A PRAZO---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_vendas", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_vendas")
            self.click()
            if not self.find( "r_vendasCaixaAPrazo", matching=0.97, waiting_time=10000):
                self.not_found("r_vendasCaixaAPrazo")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()

                            ####---R AVALIACAO DE MARGEM---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_gerencial", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_gerencial")
            self.click()
            if not self.find( "r_avaliacaoDeMargem", matching=0.97, waiting_time=10000):
                self.not_found("r_avaliacaoDeMargem")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            x=0
            while x<5:
                self.type_right()
                x=x+1
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.space()
            self.space()
            self.tab()
            x=0
            while x<5:
                self.type_right()
                x=x+1
            self.tab()
            x=0
            while x<3:
                self.type_right()
                x=x+1
            self.tab()
            x=0
            while x<3:
                self.type_right()
                x=x+1
            self.tab()
            self.type_keys_with_interval(1,'123')
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()

                            ####---R AVALIACAO VENDAS POR ITEM---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_gerencial", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_gerencial")
            self.click()
            if not self.find( "r_avaliacaoVendasPorItens", matching=0.97, waiting_time=10000):
                self.not_found("r_avaliacaoVendasPorItens")
            self.click()
            x=0
            while x<5:
                self.type_right()
                x=x+1
            self.tab()
            x=0
            while x<7:
                self.space()
                self.space()
                self.tab()
                x=x+1
            self.tab()
            self.tab()
            self.tab()
            self.type_right()
            self.tab()
            x=0
            while x<5:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            self.type_right()
            self.tab()
            self.type_right()
            self.tab()
            self.type_right()
            self.type_right()
            self.type_right()
            self.tab()
            x=0
            while x<7:
                self.type_right()
                x=x+1
            self.tab()
            x=0
            while x<4:
                self.type_right()
                x=x+1
            self.tab()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()

                            ####---R RANKING DE VENDAS---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_gerencial", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_gerencial")
            self.click()
            if not self.find( "r_rankingDeVendas", matching=0.97, waiting_time=10000):
                self.not_found("r_rankingDeVendas")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.tab()
            self.type_right()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()

                            ####---R AVALIACAO VENDA POR CLIENTE---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_gerencial", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_gerencial")
            self.click()
            if not self.find( "r_avaliacaoVendasPorCliente", matching=0.97, waiting_time=10000):
                self.not_found("r_avaliacaoVendasPorCliente")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.tab()
            x=0
            while x<6:
                self.type_right()
                x=x+1
            self.tab()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()

                            ####---R ANALISE DE ENQUETES---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_gerencial", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_gerencial")
            self.click()
            if not self.find( "r_analiseDeEnquetes", matching=0.97, waiting_time=10000):
                self.not_found("r_analiseDeEnquetes")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.tab()
            self.type_right()
            self.tab()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()

                            ####---R ANALISE DA MEDIA---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_gerencial", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_gerencial")
            self.click()
            if not self.find( "r_analiseDaMedia", matching=0.97, waiting_time=10000):
                self.not_found("r_analiseDaMedia")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            if not self.find( "op_listar_r_mediaPagamentos", matching=0.97, waiting_time=10000):
                self.not_found("op_listar_r_mediaPagamentos")
            self.click_relative(16, 160)
            self.type_right()
            self.type_right()
            if not self.find( "op_tipoRelacao_r_mediaPagamentos", matching=0.97, waiting_time=10000):
                self.not_found("op_tipoRelacao_r_mediaPagamentos")
            self.click_relative(159, 132)
            self.type_right()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()

                            ####---R CLIENTES INDICADORES---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_gerencial", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_gerencial")
            self.click()
            if not self.find( "r_clientesIndicadores", matching=0.97, waiting_time=10000):
                self.not_found("r_clientesIndicadores")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.tab()
            self.tab()
            self.tab()
            self.type_right()
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            self.tab()
            x=0
            while x<5:
                self.type_right()
                x=x+1
            self.tab()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()

                            ####---R VENDAS POR REGIONALIZACAO---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_gerencial", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_gerencial")
            self.click()
            if not self.find( "r_vendasPorRegionalizacao", matching=0.97, waiting_time=10000):
                self.not_found("r_vendasPorRegionalizacao")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.tab()
            self.tab()
            self.tab()
            x=0
            while x<7:
                self.space()
                self.space()
                self.tab()
                x=x+1
            self.type_right()
            self.tab()
            self.type_right()
            self.tab()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()

                            ####---R PEDIDOS POR REGIONALIZACAO---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_gerencial", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_gerencial")
            self.click()
            if not self.find( "r_pedidosPorRegionalizacao", matching=0.97, waiting_time=10000):
                self.not_found("r_pedidosPorRegionalizacao")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.type_right()
            self.type_right()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.tab()
            self.tab()
            self.tab()
            self.space()
            self.type_down()
            x=0
            while x<12:
                self.space()
                self.type_down()
                x=x+1
            self.tab()
            x=0
            while x<3:
                self.space()
                self.tab()
                x=x+1
            self.type_right()
            self.type_right()
            self.tab()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()

                            ####---R QUANTIDADE DE PEDIDOS VENDEDOR X ESTADOS---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_gerencial", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_gerencial")
            self.click()
            if not self.find( "r_quantidadePedidosPorVendedor", matching=0.97, waiting_time=10000):
                self.not_found("r_quantidadePedidosPorVendedor")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.type_right()
            self.type_right()
            self.tab()
            self.space()
            self.type_down()
            x=0
            while x<12:
                self.space()
                self.type_down()
                x=x+1
            self.tab()
            self.space()
            self.space()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()

                            ####---R COMPRAS POR REGIONALIZACAO---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_gerencial", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_gerencial")
            self.click()
            if not self.find( "r_comprasPorRegionalizacao", matching=0.97, waiting_time=10000):
                self.not_found("r_comprasPorRegionalizacao")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.tab()
            self.tab()
            self.tab()
            x=0
            while x<5:
                self.space()
                self.space()
                self.tab()
                x=x+1
            self.type_right()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()

                            ####---R PEDIDOS DE COMPRA POR REGIONALIZACAO---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_gerencial", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_gerencial")
            self.click()
            if not self.find( "r_pedidosCompraRegionalizacao", matching=0.97, waiting_time=10000):
                self.not_found("r_pedidosCompraRegionalizacao")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.type_right()
            self.type_right()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.space()
            x=0
            while x<4:
                self.space()
                self.type_down()
                x=x+1
            self.tab()
            x=0
            while x<3:
                self.space()
                self.space()
                self.tab()
                x=x+1
            self.type_right()
            self.type_right()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtros_plural", matching=0.97, waiting_time=10000):
                self.not_found("filtros_plural")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()

                            ####---R AVALIACAO COMPRA POR ITENS---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_gerencial", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_gerencial")
            self.click()
            if not self.find( "r_avaliacaoComprasItem", matching=0.97, waiting_time=10000):
                self.not_found("r_avaliacaoComprasItem")
            self.click()
            self.type_right()
            self.type_right()
            self.type_right()
            self.tab()
            x=0
            while x<5:
                self.space()
                self.space()
                self.tab()
                x=x+1
            self.type_right()
            self.type_right()
            self.tab()
            self.type_right()
            self.type_right()
            self.type_right()
            self.tab()
            x=0
            while x<6:
                self.type_right()
                x=x+1
            self.tab()
            self.tab()
            self.tab()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            x=0
            while x<4:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()

                            ####---R FLUXO DE CAIXA DIARIO---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_gerencial", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_gerencial")
            self.click()
            if not self.find( "r_fluxoCaixaDiario", matching=0.97, waiting_time=10000):
                self.not_found("r_fluxoCaixaDiario")
            self.click()
            self.space()
            self.space()
            self.tab()
            x=0
            while x<5:
                self.type_right()
                x=x+1
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            self.tab()
            x=0
            while x<4:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R COMPARATIVO FRETES NEGOCIADOS---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_gerencial", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_gerencial")
            self.click()
            if not self.find( "r_fluxoDeCaixaDiarioProjetado", matching=0.97, waiting_time=10000):
                self.not_found("r_fluxoDeCaixaDiarioProjetado")
            self.click()
            self.space()
            self.space()
            self.tab()
            x=0
            while x<5:
                self.type_right()
                x=x+1
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()

                            ####---R COMPARATIVO FRETES NEGOCIADOS---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_gerencial", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_gerencial")
            self.click()
            if not self.find( "r_comparativoFretesNegociados", matching=0.97, waiting_time=10000):
                self.not_found("r_comparativoFretesNegociados")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()

                            ####---R ACOMPANHAMENTO GLOBAL---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_gerencial", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_gerencial")
            self.click()
            if not self.find( "r_acompanhamentoGlobal", matching=0.97, waiting_time=10000):
                self.not_found("r_acompanhamentoGlobal")
            self.click()
            x=0
            while x<5:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()

                            ####---R EVOLUCAO MENSAL---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_gerencial", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_gerencial")
            self.click()
            if not self.find( "r_evolucaoMensal", matching=0.97, waiting_time=10000):
                self.not_found("r_evolucaoMensal")
            self.click()
            x=0
            while x<10:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()

                            ####---R CLIENTES POR CLASSIFICACAO---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_gerencial", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_gerencial")
            self.click()
            if not self.find( "r_clientesPorClassificacao", matching=0.97, waiting_time=10000):
                self.not_found("r_clientesPorClassificacao")
            self.click()
            x=0
            while x<2:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()

                            ####---R COMISSOES BASEADAS NOS ITENS---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_comissoes", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_comissoes")
            self.click()
            if not self.find( "r_mov_c_baseItens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_c_baseItens")
            self.click()
            if not self.find( "r_comissaoCalculadaBaseItem", matching=0.97, waiting_time=10000):
                self.not_found("r_comissaoCalculadaBaseItem")
            self.click()
            x=0
            while x<5:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.space()
            self.space()
            self.tab()
            self.tab()
            self.tab()
            self.tab()
            self.tab()
            self.space()
            self.space()
            self.tab()
            self.space()
            self.space()
            self.tab()
            self.tab()
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            x=0
            while x<6:
                self.space()
                self.space()
                self.tab()
                x=x+1
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            ######################################################################################
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_comissoes", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_comissoes")
            self.click()
            if not self.find( "r_mov_c_baseItens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_c_baseItens")
            self.click()
            if not self.find( "r_comissaoItensDevolvidos", matching=0.97, waiting_time=10000):
                self.not_found("r_comissaoItensDevolvidos")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.tab()
            self.type_right()
            self.type_right()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            #####################################################################################
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_comissoes", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_comissoes")
            self.click()
            if not self.find( "r_mov_c_baseItens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_c_baseItens")
            self.click()
            if not self.find( "r_comissaoComBaseComissao", matching=0.97, waiting_time=10000):
                self.not_found("r_comissaoComBaseComissao")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            self.type_right()
            self.type_right()
            self.type_right()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()

                            ####---R COMISSAO COM BASE NO FINANCEIRO---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_comissoes", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_comissoes")
            self.click()
            if not self.find( "r_comissaoComBaseNoFinanceiro", matching=0.97, waiting_time=10000):
                self.not_found("r_comissaoComBaseNoFinanceiro")
            self.click()
            if not self.find( "r_FinanceiroPComissao", matching=0.97, waiting_time=10000):
                self.not_found("r_FinanceiroPComissao")
            self.click()
            x=0
            while x<4:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            x=0
            while x<5:
                self.tab()
                x=x+1
            self.type_right()
            self.type_right()
            self.tab()
            self.type_right()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.tab()
            x=0
            while x<7:
                self.type_right()
                x=x+1
            self.tab()
            self.type_right()
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            ######################################################################################
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_comissoes", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_comissoes")
            self.click()
            if not self.find( "r_comissaoComBaseNoFinanceiro", matching=0.97, waiting_time=10000):
                self.not_found("r_comissaoComBaseNoFinanceiro")
            self.click()
            if not self.find( "r_financeiroPItens", matching=0.97, waiting_time=10000):
                self.not_found("r_financeiroPItens")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_left()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.tab()
            self.type_right()
            x=0
            while x<3:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.type_left()
            self.type_left()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.type_right()
            self.type_right()
            self.type_right()
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            self.type_right()
            self.tab()
            self.type_right()
            self.tab()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            ########################################################################################
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_comissoes", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_comissoes")
            self.click()
            if not self.find( "r_comissaoComBaseNoFinanceiro", matching=0.97, waiting_time=10000):
                self.not_found("r_comissaoComBaseNoFinanceiro")
            self.click()
            if not self.find( "r_financeiroPInformado", matching=0.97, waiting_time=10000):
                self.not_found("r_financeiroPInformado")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_left()
            self.type_left()
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            self.type_right()
            self.type_right()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()

                            ####---R COMISSOES FORCHE---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_comissoes", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_comissoes")
            self.click()
            if not self.find( "r_mov_comissoes_especificos", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_comissoes_especificos")
            self.click()
            if not self.find( "r_comissoesForche", matching=0.97, waiting_time=10000):
                self.not_found("r_comissoesForche")
            self.click()
            self.type_right()
            self.tab()
            self.type_right()
            self.type_right()
            self.type_right()
            self.tab()
            x=0
            while x<6:
                self.type_right()
                x=x+1
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()

                            ####---R ETIQUETAS---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_emissoes", matching=0.97, waiting_time=10000):
                self.not_found("r_emissoes")
            self.click()
            if not self.find( "r_emissoes_etiquetas", matching=0.97, waiting_time=10000):
                self.not_found("r_emissoes_etiquetas")
            self.click()
            if not self.find( "r_emissoes_etiquetas_clientes", matching=0.97, waiting_time=10000):
                self.not_found("r_emissoes_etiquetas_clientes")
            self.click()
            if not self.find( "ir_emissaoEtiquetas", matching=0.97, waiting_time=10000):
                self.not_found("ir_emissaoEtiquetas")
            self.click_relative(13, 110)
            self.wait(1000)
            if not self.find( "selecionar_consultaClientes", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_consultaClientes")
            self.click_relative(34, 502)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "informacao_singular", matching=0.97, waiting_time=10000):
                self.not_found("informacao_singular")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.type_right()
            self.enter()
            #if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
            #    self.not_found("retornarpe")
            #self.click()

                            ####---R ETIQUETAS ITENS---####
            """                 
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_emissoes", matching=0.97, waiting_time=10000):
                self.not_found("r_emissoes")
            self.click()
            if not self.find( "r_emissoes_etiquetas", matching=0.97, waiting_time=10000):
                self.not_found("r_emissoes_etiquetas")
            self.click()
            if not self.find( "r_etiquetas_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_etiquetas_itens")
            self.click()
            if not self.find( "ir_etiquetaItens", matching=0.97, waiting_time=10000):
                self.not_found("ir_etiquetaItens")
            self.click_relative(13, 110)
            if not self.find( "b_itens_etiquetas", matching=0.97, waiting_time=10000):
                self.not_found("b_itens_etiquetas")
            self.click_relative(11, 33)
            self.type_keys_with_interval(1,'104455')
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.type_keys_with_interval(1,'1')
            self.tab()
            self.enter()
            self.wait(500)
            self.type_right()
            self.enter()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "a3_r_etiquetaItens", matching=0.97, waiting_time=10000):
                self.not_found("a3_r_etiquetaItens")
            self.click()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            if not self.find( "a4_r_etiquetaItens", matching=0.97, waiting_time=10000):
                self.not_found("a4_r_etiquetaItens")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            self.tab()
            self.type_right()
            self.tab()
            if not self.find( "b_condicaoPagamento_r_etiquetaItens", matching=0.97, waiting_time=10000):
                self.not_found("b_condicaoPagamento_r_etiquetaItens")
            self.click_relative(76, 201)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_planoPreco1_r_etiquetaItens", matching=0.97, waiting_time=10000):
                self.not_found("b_planoPreco1_r_etiquetaItens")
            self.click_relative(77, 247)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_planoPreco2_r_etiquetaItens", matching=0.97, waiting_time=10000):
                self.not_found("b_planoPreco2_r_etiquetaItens")
            self.click_relative(532, 249)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "informacao_singular", matching=0.97, waiting_time=10000):
                self.not_found("informacao_singular")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.type_right()
            self.enter()
            self.key_esc()
            #if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
            #    self.not_found("retornarpe")
            #self.click()
            """
                            ####---R BOLETO BANCARIO---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_emissoes", matching=0.97, waiting_time=10000):
                self.not_found("r_emissoes")
            self.click()
            if not self.find( "r_boletoBancario", matching=0.97, waiting_time=10000):
                self.not_found("r_boletoBancario")
            self.click()
            self.tab()
            x=0
            while x<4:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.type_down()
            self.type_down()
            self.type_up()
            self.type_up()
            self.tab()
            self.type_right()
            self.tab()
            self.type_right()
            self.tab()
            x=0
            while x<4:
                self.type_right()
                x=x+1
            self.tab()
            x=0
            while x<4:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.tab()
            self.tab()
            self.type_right()
            self.tab()
            x=0
            while x<4:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.type_right()
            self.type_right()
            if not self.find( "filtro_plural", matching=0.97, waiting_time=10000):
                self.not_found("filtro_plural")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()

                            ####---R CARNES---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_emissoes", matching=0.97, waiting_time=10000):
                self.not_found("r_emissoes")
            self.click()
            if not self.find( "r_carnes", matching=0.97, waiting_time=10000):
                self.not_found("r_carnes")
            self.click()
            self.tab()
            x=0
            while x<4:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.type_down()
            self.type_down()
            self.type_up()
            self.type_up()
            self.tab()
            self.type_right()
            self.tab()
            self.type_right()
            self.tab()
            x=0
            while x<4:
                self.type_right()
                x=x+1
            self.tab()
            x=0
            while x<4:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.tab()
            if not self.find( "filtro_plural", matching=0.97, waiting_time=10000):
                self.not_found("filtro_plural")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()

                            ####---R DUPLICATAS---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_emissoes", matching=0.97, waiting_time=10000):
                self.not_found("r_emissoes")
            self.click()
            if not self.find( "r_duplicatas", matching=0.97, waiting_time=10000):
                self.not_found("r_duplicatas")
            self.click()
            self.tab()
            x=0
            while x<4:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.type_down()
            self.type_down()
            self.type_up()
            self.type_up()
            self.tab()
            self.type_right()
            self.tab()
            self.type_right()
            self.tab()
            x=0
            while x<4:
                self.type_right()
                x=x+1
            self.tab()
            x=0
            while x<4:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.tab()
            if not self.find( "filtro_plural", matching=0.97, waiting_time=10000):
                self.not_found("filtro_plural")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R FATURAS ---####
            
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_emissoes", matching=0.97, waiting_time=10000):
                self.not_found("r_emissoes")
            self.click()                 
            if not self.find( "r_faturas", matching=0.97, waiting_time=10000):
                self.not_found("r_faturas")
            self.click()
            x=0
            while x<4:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.tab()
            self.tab()
            self.space()
            self.space()
            self.tab()
            self.type_right()
            self.type_right()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()

                            ####---R AVISO RECEBIMENTO---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_emissoes", matching=0.97, waiting_time=10000):
                self.not_found("r_emissoes")
            self.click()      
            if not self.find( "r_avisoRecebimento", matching=0.97, waiting_time=10000):
                self.not_found("r_avisoRecebimento")
            self.click()
            if not self.find( "b_municipio_r_avisoRecebimento", matching=0.97, waiting_time=10000):
                self.not_found("b_municipio_r_avisoRecebimento")
            self.click_relative(64, 85)
            self.type_keys_with_interval(1,'guarapuava')
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'a1')
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R APURACAO PIS COFINS---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_controladoria", matching=0.97, waiting_time=10000):
                self.not_found("r_controladoria")
            self.click()
            if not self.find( "r_apuracaoPISCOFINS", matching=0.97, waiting_time=10000):
                self.not_found("r_apuracaoPISCOFINS")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.tab()
            self.space()
            self.space()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()

                            ####---R RELACAO DIFAL FCP---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_controladoria", matching=0.97, waiting_time=10000):
                self.not_found("r_controladoria")
            self.click()
            if not self.find( "r_relacaoDIFAL_FCP", matching=0.97, waiting_time=10000):
                self.not_found("r_relacaoDIFAL_FCP")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()

                            ####---R RELACAO DOCUMENTOS IMITIDOS---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_controladoria", matching=0.97, waiting_time=10000):
                self.not_found("r_controladoria")
            self.click()
            if not self.find( "r_relacaoDocumentosImitidos", matching=0.97, waiting_time=10000):
                self.not_found("r_relacaoDocumentosImitidos")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()

                            ####---R DRE---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_controladoria", matching=0.97, waiting_time=10000):
                self.not_found("r_controladoria")
            self.click()
            if not self.find( "r_DRE", matching=0.97, waiting_time=10000):
                self.not_found("r_DRE")
            self.click()
            x=0
            while x<8:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.tab()
            self.tab()
            self.space()
            self.space()
            self.tab()
            self.space()
            self.space()
            self.tab()
            self.tab()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.space()
            self.space()
            self.tab()
            self.space()
            self.space()
            self.tab()
            if not self.find( "b_moedas_r_demonstrativoResultado", matching=0.97, waiting_time=10000):
                self.not_found("b_moedas_r_demonstrativoResultado")
            self.click_relative(57, 235)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_livroOficial_r_demonstrativoResultado", matching=0.97, waiting_time=10000):
                self.not_found("b_livroOficial_r_demonstrativoResultado")
            self.click_relative(187, 180)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            if not self.find( "b_grupoEmpresa_r_demonstrativoResultado", matching=0.97, waiting_time=10000):
                self.not_found("b_grupoEmpresa_r_demonstrativoResultado")
            self.click_relative(272, 181)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            x=0
            while x<9:
                self.tab()
                x=x+1
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()

                            ####---R BALANCETE---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_controladoria", matching=0.97, waiting_time=10000):
                self.not_found("r_controladoria")
            self.click()
            if not self.find( "r_balancete", matching=0.97, waiting_time=10000):
                self.not_found("r_balancete")
            self.click()
            x=0
            while x<7:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.tab()
            self.tab()
            self.tab()
            x=0
            while x<6:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            x=0
            while x<10:
                self.space()
                self.space()
                self.tab()
                x=x+1
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            if not self.find( "b_moedas_r_emissaoBalancete", matching=0.97, waiting_time=10000):
                self.not_found("b_moedas_r_emissaoBalancete")
            self.click_relative(56, 343)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            if not self.find( "informacoes", matching=0.97, waiting_time=10000):
                self.not_found("informacoes")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()

                            ####---R GERACAO SINTEGRA---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_controladoria", matching=0.97, waiting_time=10000):
                self.not_found("r_controladoria")
            self.click()
            if not self.find( "r_geracaoSintegra", matching=0.97, waiting_time=10000):
                self.not_found("r_geracaoSintegra")
            self.click()
            if not self.find( "b_empresa_r_validaSintegra", matching=0.97, waiting_time=10000):
                self.not_found("b_empresa_r_validaSintegra")
            self.click_relative(196, 81)
            self.tab()
            self.tab()
            self.tab()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'01012024')
            self.tab()
            self.type_keys_with_interval(1,'01012024')
            self.tab()
            self.tab()
            self.type_up()
            self.tab()
            self.type_up()
            self.type_up()
            self.tab()
            self.type_up()
            self.type_up()
            self.type_up()
            self.type_up()
            self.tab()
            self.type_up()
            self.type_down()
            self.tab()
            x=0
            while x<5:
                self.type_down()
                x=x+1
            self.tab()
            self.type_keys_with_interval(1,'01012024')
            self.tab()
            x=0
            while x<2:
                self.space()
                self.space()
                self.tab()
                x=x+1
            self.type_keys_with_interval(1,'01012024')
            self.tab()
            x=0
            while x<12:
                self.space()
                self.space()
                self.tab()
                x=x+1
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()

                            ####---R GERACAO QUESTOR---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_controladoria", matching=0.97, waiting_time=10000):
                self.not_found("r_controladoria")
            self.click()
            if not self.find( "r_geracaoQuestor", matching=0.97, waiting_time=10000):
                self.not_found("r_geracaoQuestor")
            self.click()
            self.type_keys_with_interval(1,'1203')
            self.tab()
            self.type_keys_with_interval(1,'1203')
            self.tab()
            self.tab()
            self.space()
            self.space()
            self.tab()
            self.tab()
            self.space()
            self.space()
            self.tab()
            if not self.find( "filtro_plural", matching=0.97, waiting_time=10000):
                self.not_found("filtro_plural")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "fechargestaoadm", matching=0.97, waiting_time=10000):
                self.not_found("fechargestaoadm")
            self.click()
            if not self.find( "simfecharfim", matching=0.97, waiting_time=10000):
                self.not_found("simfecharfim")
            self.click()

def not_found(self, label):
                print(f"Element not found: {label}")  
        
if __name__ == '__main__':
    Bot.main()








































































































































































































