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
            if not self.find( "aba_precos", matching=0.97, waiting_time=10000):
                self.not_found("aba_precos")
            self.click()
            self.wait(1500)
            self.type_down()
            self.type_down()
            self.wait(1500)
            if not self.find( "ofertas_campanhas_panfletos_precos", matching=0.97, waiting_time=10000):
                self.not_found("ofertas_campanhas_panfletos_precos")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "ir_movimento_oep", matching=0.97, waiting_time=10000):
                self.not_found("ir_movimento_oep")
            self.click_relative(8, 266)
            if not self.find( "buscaritensreqcompras", matching=0.97, waiting_time=10000):
                self.not_found("buscaritensreqcompras")
            self.click_relative(10, 31)
            self.type_keys_with_interval(1,'agulha gengival')
            self.enter()
            self.type_down()
            self.type_down()
            self.type_down()
            self.type_down()
            self.wait(500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "botaoconfirmaritensreqcompras", matching=0.97, waiting_time=10000):
                self.not_found("botaoconfirmaritensreqcompras")
            self.click()
            self.wait(3000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.wait(3000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "op_todas_movtransitens", matching=0.97, waiting_time=10000):
                self.not_found("op_todas_movtransitens")
            self.click()            
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                self.not_found("simexcluirrs")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---PRECOS DA CONCORRENCIA---####
                             
            if not self.find( "aba_precos", matching=0.97, waiting_time=10000):
                self.not_found("aba_precos")
            self.click()
            if not self.find( "precosdaconcorrencia_precos", matching=0.97, waiting_time=10000):
                self.not_found("precosdaconcorrencia_precos")
            self.click()
            self.enter()
            if not self.find( "aba2_consultadevolucaoitens", matching=0.97, waiting_time=10000):
                self.not_found("aba2_consultadevolucaoitens")
            self.click()
            if not self.find( "b_item_movimentoconcorrencia", matching=0.97, waiting_time=10000):
                self.not_found("b_item_movimentoconcorrencia")
            self.click_relative(77, 153)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_fornecedor_movconcorrencia", matching=0.97, waiting_time=10000):
                self.not_found("b_fornecedor_movconcorrencia")
            self.click_relative(378, 83)
            self.enter()
            x=0
            while x<18:
                self.type_down()
                x=x+1
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "ir_pesquisaconcorrente", matching=0.97, waiting_time=10000):
                self.not_found("ir_pesquisaconcorrente")
            self.click_relative(14, 148)
            self.wait(1500)
            if not self.find( "ir_precoFornecedorConcorrencia", matching=0.97, waiting_time=10000):
                self.not_found("ir_precoFornecedorConcorrencia")
            self.click_relative(12, 149)
            if not self.find( "buscaritensreqcompras", matching=0.97, waiting_time=10000):
                self.not_found("buscaritensreqcompras")
            self.click_relative(10, 31)
            self.type_keys_with_interval(1,'agulha gengival')
            self.enter()
            self.type_down()
            self.type_down()
            self.type_down()
            self.type_down()
            self.wait(500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "botaoconfirmaritensreqcompras", matching=0.97, waiting_time=10000):
                self.not_found("botaoconfirmaritensreqcompras")
            self.click()
            self.type_right()
            self.enter()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()           
            if not self.find( "cod_1_fornecedor_concorrencia", matching=0.97, waiting_time=100000):
                self.not_found("cod_1_fornecedor_concorrencia")
            self.click()
            if not self.find( "b_fornecedor_fornecedorConcorrencia", matching=0.97, waiting_time=10000):
                self.not_found("b_fornecedor_fornecedorConcorrencia")
            self.click_relative(71, 80)
            self.enter()
            self.type_down()
            self.type_down()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "gravar_fornecedorConcorrencia", matching=0.97, waiting_time=10000):
                self.not_found("gravar_fornecedorConcorrencia")
            self.click()
            self.wait(500)                   
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.wait(500)
            self.enter()
            self.wait(500)
            self.enter()
            if not self.find( "aba2_mvPesquisaConcorrentes", matching=0.97, waiting_time=10000):
                self.not_found("aba2_mvPesquisaConcorrentes")
            self.click()
            if not self.find( "ir_pesquisaconcorrente", matching=0.97, waiting_time=10000):
                self.not_found("ir_pesquisaconcorrente")
            self.click_relative(14, 148)           
            self.wait(1500)
            if not self.find( "ir_precoFornecedorConcorrencia", matching=0.97, waiting_time=10000):
                self.not_found("ir_precoFornecedorConcorrencia")
            self.click_relative(12, 149)           
            self.wait(500)
            if not self.find( "buscaritensreqcompras", matching=0.97, waiting_time=10000):
                self.not_found("buscaritensreqcompras")
            self.click_relative(10, 31)
            self.type_keys_with_interval(1,'agulha gengival')
            self.enter()
            self.type_down()
            self.type_down()
            self.type_down()
            self.type_down()
            self.wait(500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "botaoconfirmaritensreqcompras", matching=0.97, waiting_time=10000):
                self.not_found("botaoconfirmaritensreqcompras")
            self.click()
            self.type_right()
            self.enter()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "cod_1_fornecedor_concorrencia", matching=0.97, waiting_time=100000):
                self.not_found("cod_1_fornecedor_concorrencia")
            self.click()
            if not self.find( "b_fornecedor_fornecedorConcorrencia", matching=0.97, waiting_time=10000):
                self.not_found("b_fornecedor_fornecedorConcorrencia")
            self.click_relative(71, 80)
            self.enter()
            self.type_down()
            self.type_down()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "gravar_fornecedorConcorrencia", matching=0.97, waiting_time=10000):
                self.not_found("gravar_fornecedorConcorrencia")
            self.click()           
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                self.not_found("simexcluirrs")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---PRECOS POR FORNECEDORES---####
                             
            if not self.find( "aba_precos", matching=0.97, waiting_time=10000):
                self.not_found("aba_precos")
            self.click()
            if not self.find( "precosPorFornecedores", matching=0.97, waiting_time=10000):
                self.not_found("precosPorFornecedores")
            self.click()
            if not self.find( "b_fornecedor_movPrecosFornecedor", matching=0.97, waiting_time=10000):
                self.not_found("b_fornecedor_movPrecosFornecedor")
            self.click_relative(291, 85)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_item_movPrecoFornecedor", matching=0.97, waiting_time=10000):
                self.not_found("b_item_movPrecoFornecedor")
            self.click_relative(701, 84)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            if not self.find( "b_fornecedor_precosFornecedor", matching=0.97, waiting_time=10000):
                self.not_found("b_fornecedor_precosFornecedor")
            self.click_relative(75, 82)
            self.enter()
            self.type_down()
            self.type_down()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "ir_precosPorFornecedor", matching=0.97, waiting_time=10000):
                self.not_found("ir_precosPorFornecedor")
            self.click_relative(13, 150)
            if not self.find( "buscaritensreqcompras", matching=0.97, waiting_time=10000):
                self.not_found("buscaritensreqcompras")
            self.click_relative(10, 31)
            
            self.type_keys_with_interval(1,'agulha gengival')
            self.enter()
            self.type_down()
            self.type_down()
            self.type_down()
            self.type_down()
            self.wait(500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "botaoconfirmaritensreqcompras", matching=0.97, waiting_time=10000):
                self.not_found("botaoconfirmaritensreqcompras")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.wait(1000)
            if not self.find( "gravar_fornecedorConcorrencia", matching=0.97, waiting_time=10000):
                self.not_found("gravar_fornecedorConcorrencia")
            self.click()
            self.wait(3000)
            """
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()  
            self.enter()
            self.wait(500)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab() 
            #if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
            #    self.not_found("retornarpe")
            #self.click()
            self.wait(1000)
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()"""
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.enter()
            self.wait(60000)
            #if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
            #    self.not_found("retornarpe")
            #self.click()
            #self.enter()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.type_right()
            self.enter()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            #self.enter()
            #if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
            #    self.not_found("retornarpe")
            #self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---TABELA DE PRECOS POR FORNECEDOR---####
                             
            if not self.find( "aba_precos", matching=0.97, waiting_time=10000):
                self.not_found("aba_precos")
            self.click()
            if not self.find( "tabelaPrecosFornecedor", matching=0.97, waiting_time=10000):
                self.not_found("tabelaPrecosFornecedor")
            self.click()
            self.enter()
            if not self.find( "aba2_consultadevolucaoitens", matching=0.97, waiting_time=10000):
                self.not_found("aba2_consultadevolucaoitens")
            self.click()
            if not self.find( "b_item_TabelaPrecoFornecedor", matching=0.97, waiting_time=10000):
                self.not_found("b_item_TabelaPrecoFornecedor")
            self.click_relative(76, 154)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_fornecedor_TabelaPrecosFornecedor", matching=0.97, waiting_time=10000):
                self.not_found("b_fornecedor_TabelaPrecosFornecedor")
            self.click_relative(373, 82)
            self.enter()
            x=0
            while x<18:
                self.type_down()
                x=x+1
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "b_fornecedor_TabelaDePrecosFornecedor", matching=0.97, waiting_time=10000):
                self.not_found("b_fornecedor_TabelaDePrecosFornecedor")
            self.click_relative(157, 119)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "ir_TabelaPrecosPorFornecedor", matching=0.97, waiting_time=10000):
                self.not_found("ir_TabelaPrecosPorFornecedor")
            self.click_relative(13, 169)
            if not self.find( "buscaritensreqcompras", matching=0.97, waiting_time=10000):
                self.not_found("buscaritensreqcompras")
            self.click_relative(10, 31)
            self.type_keys_with_interval(1,'agulha gengival')
            self.enter()
            self.type_down()
            self.type_down()
            self.type_down()
            self.type_down()
            self.wait(500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            if not self.find( "botaoconfirmaritensreqcompras", matching=0.97, waiting_time=10000):
                self.not_found("botaoconfirmaritensreqcompras")
            self.click()
            self.wait(1000)
            self.enter()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.wait(500)
            self.enter()
            if not self.find( "cancelar_teste2", matching=0.97, waiting_time=10000):
                self.not_found("cancelar_teste2")
            self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.wait(500)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.wait(500)
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            self.wait(500)
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                self.not_found("simexcluirrs")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---PRECIFICACAO---####
                             
            if not self.find( "aba_precos", matching=0.97, waiting_time=10000):
                self.not_found("aba_precos")
            self.click()
            if not self.find( "precificacao", matching=0.97, waiting_time=10000):
                self.not_found("precificacao")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "calcular", matching=0.97, waiting_time=10000):
                self.not_found("calcular")
            self.click()
            self.enter()
            """if not self.find( "b_operacao_calculoPrecos", matching=0.97, waiting_time=10000):
                self.not_found("b_operacao_calculoPrecos")
            self.click_relative(66, 198)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_regiao_calculoPrecos", matching=0.97, waiting_time=10000):
                self.not_found("b_regiao_calculoPrecos")
            self.click_relative(431, 198)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_grupoFiscal_calculoPrecos", matching=0.97, waiting_time=10000):
                self.not_found("b_grupoFiscal_calculoPrecos")
            self.click_relative(665, 198)
            self.tab()
            self.tab()
            self.tab()
            self.type_down()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "retornar_calculoDePrecos", matching=0.97, waiting_time=10000):
                self.not_found("retornar_calculoDePrecos")
            self.click_relative(26, 36)
            """
            self.key_esc()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---GRUPOS DE CAMPANHAS---####
                             
            if not self.find( "aba_precos", matching=0.97, waiting_time=10000):
                self.not_found("aba_precos")
            self.click()
            if not self.find( "gruposdecampanhas", matching=0.97, waiting_time=10000):
                self.not_found("gruposdecampanhas")
            self.click()
            self.enter()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "ir_movimentoGrupoDeCampanha", matching=0.97, waiting_time=10000):
                self.not_found("ir_movimentoGrupoDeCampanha")
            self.click_relative(10, 135)
            if not self.find( "buscaritensreqcompras", matching=0.97, waiting_time=10000):
                self.not_found("buscaritensreqcompras")
            self.click_relative(10, 31)
            self.type_keys_with_interval(1,'agulha gengival')
            self.enter()
            self.type_down()
            self.type_down()
            self.type_down()
            self.type_down()
            self.wait(500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "botaoconfirmaritensreqcompras", matching=0.97, waiting_time=10000):
                self.not_found("botaoconfirmaritensreqcompras")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.wait(7000)
            #self.key_esc()
            #if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
            #    self.not_found("retornarpe")
            #self.click()
            self.wait(2000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.wait(1000)
            #self.key_esc()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.wait(500)
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            self.wait(500)
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            self.wait(500)
            if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                self.not_found("simexcluirrs")
            self.click()
            self.wait(500)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---CAMPANHAS---####
                             
            if not self.find( "aba_precos", matching=0.97, waiting_time=10000):
                self.not_found("aba_precos")
            self.click()
            if not self.find( "campanhas", matching=0.97, waiting_time=10000):
                self.not_found("campanhas")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            x=0
            while x<2:
                y=0
                while y<2:
                    self.tab()
                    self.type_keys_with_interval(1,'123')
                    y=y+1
                x=x+1
            self.tab()
            x=0
            while x<3:
                self.type_down()
                x=x+1
            if not self.find( "ir_movimentoCampanhas", matching=0.97, waiting_time=10000):
                self.not_found("ir_movimentoCampanhas")
            self.click_relative(10, 178)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "aba2_movimentoCampanhas", matching=0.97, waiting_time=10000):
                self.not_found("aba2_movimentoCampanhas")
            self.click()
            if not self.find( "ir_movimentoCampanhas", matching=0.97, waiting_time=10000):
                self.not_found("ir_movimentoCampanhas")
            self.click_relative(10, 178)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            if not self.find( "aba3_movimentoCampanhas", matching=0.97, waiting_time=10000):
                self.not_found("aba3_movimentoCampanhas")
            self.click()
            if not self.find( "ir_movimentoCampanhas", matching=0.97, waiting_time=10000):
                self.not_found("ir_movimentoCampanhas")
            self.click_relative(10, 178)
            if not self.find( "b_F2_codigoReferencia", matching=0.97, waiting_time=10000):
                self.not_found("b_F2_codigoReferencia")
            self.click_relative(-13, 63)
            self.enter()
            x=0
            while x<31:
                self.type_down()
                x=x+1
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.type_keys_with_interval(1,'123')
            self.tab()
            x=0
            while x<4:
                self.type_down()
                x=x+1
            x=0
            while x<3:
                self.tab()
                self.type_keys_with_interval(1,'123')
                x=x+1
            self.tab()
            self.tab()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "op_todas_movtransitens", matching=0.97, waiting_time=10000):
                self.not_found("op_todas_movtransitens")
            self.click()
            if not self.find( "data", matching=0.97, waiting_time=10000):
                self.not_found("data")
            self.click_relative(33, 7)
            if not self.find( "data_ano", matching=0.97, waiting_time=10000):
                self.not_found("data_ano")
            self.click()
            if not self.find( "data_ano_atual", matching=0.97, waiting_time=10000):
                self.not_found("data_ano_atual")
            self.click()             
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                self.not_found("simexcluirrs")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---FINANCEIRO---####
            
            if not self.find( "financeiro", matching=0.97, waiting_time=10000):
                self.not_found("financeiro")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "contas_receberPagar", matching=0.97, waiting_time=10000):
                self.not_found("contas_receberPagar")
            self.click()
            if not self.find( "b_botaobuscar_substituicaoteste", matching=0.97, waiting_time=10000):
                self.not_found("b_botaobuscar_substituicaoteste")
            self.click_relative(80, 122)
            self.enter()
            x=0
            while x<18:
                self.type_down()
                x=x+1
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.wait(500)
            self.type_keys_with_interval(1,'8748')
            self.tab()
            self.tab()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'123')
            if not self.find( "b_cliente_movFinanceiraContasReceber", matching=0.97, waiting_time=10000):
                self.not_found("b_cliente_movFinanceiraContasReceber")
            self.click_relative(211, 158)
            self.wait(500)
            self.enter()
            self.wait(2000)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'12312312312312312312312312312312312312312312')
            self.tab()
            self.type_keys_with_interval(1,'123')
            if not self.find( "b_condPagamento_contasReceber", matching=0.97, waiting_time=10000):
                self.not_found("b_condPagamento_contasReceber")
            self.click_relative(464, 238)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_vendedor_ContasReceber", matching=0.97, waiting_time=10000):
                self.not_found("b_vendedor_ContasReceber")
            self.click_relative(72, 276)
            self.enter()
            self.wait(500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_centroContabilizacao_ContasReceber", matching=0.97, waiting_time=10000):
                self.not_found("b_centroContabilizacao_ContasReceber")
            self.click_relative(495, 276)           
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'te12@!')
            self.tab()
            self.type_keys_with_interval(1,'te12@!')
            if not self.find( "aba1.2.1_ContasReceber", matching=0.97, waiting_time=10000):
                self.not_found("aba1.2.1_ContasReceber")
            self.click()
            if not self.find( "aba1.2.2_ContasReceber", matching=0.97, waiting_time=10000):
                self.not_found("aba1.2.2_ContasReceber")
            self.click()
            if not self.find( "b_classificacao_dadosParcela", matching=0.97, waiting_time=10000):
                self.not_found("b_classificacao_dadosParcela")
            self.click_relative(75, 38)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_planoFinanceiro_ContasReceber", matching=0.97, waiting_time=10000):
                self.not_found("b_planoFinanceiro_ContasReceber")
            self.click_relative(84, 79)
            self.type_keys_with_interval(1,'agua')
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_sacadorAvalista_ContasReceber", matching=0.97, waiting_time=10000):
                self.not_found("b_sacadorAvalista_ContasReceber")
            self.click_relative(75, 116)
            self.enter()
            self.wait(2000)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_contabilancamento_ContasReceber", matching=0.97, waiting_time=10000):
                self.not_found("b_contabilancamento_ContasReceber")
            self.click_relative(475, 40)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_contavilbaixa_ContasReceber", matching=0.97, waiting_time=10000):
                self.not_found("b_contavilbaixa_ContasReceber")
            self.click_relative(473, 76)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_comissao_ContasReceber", matching=0.97, waiting_time=10000):
                self.not_found("b_comissao_ContasReceber")
            self.click_relative(475, 116)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_localCobranca_ContasReceber", matching=0.97, waiting_time=10000):
                self.not_found("b_localCobranca_ContasReceber")
            self.click_relative(875, 37)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_pagamentoPrevisto_ContasReceber", matching=0.97, waiting_time=10000):
                self.not_found("b_pagamentoPrevisto_ContasReceber")
            self.click_relative(876, 76)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_centroCusto_ContasReceber", matching=0.97, waiting_time=10000):
                self.not_found("b_centroCusto_ContasReceber")
            self.click_relative(886, 113)
            self.backspace()
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.backspace()
            self.tab()
            if not self.find( "aba2_contasReceber", matching=0.97, waiting_time=10000):
                self.not_found("aba2_contasReceber")
            self.click()
            if not self.find( "tipolancamento_ContasReceber", matching=0.97, waiting_time=10000):
                self.not_found("tipolancamento_ContasReceber")
            self.double_click_relative(372, 161)
            x=0
            while x<4:
                self.type_down()
                x=x+1
            x=0
            while x<2:
                self.type_down()
                x=x+1
            self.tab()
            x=0
            while x<7:
                self.type_down()
                x=x+1
            if not self.find( "b_propriedade_contasReceber", matching=0.97, waiting_time=10000):
                self.not_found("b_propriedade_contasReceber")
            self.click_relative(74, 212)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.tab()
            self.tab()
            self.space()
            self.space()
            self.tab()
            if not self.find( "aba3_contasReceber", matching=0.97, waiting_time=10000):
                self.not_found("aba3_contasReceber")
            self.click()
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.wait(2000)
            self.backspace()
            self.tab()
            self.tab()
            self.backspace()
            self.type_keys_with_interval(1,'8748')
            x=0
            while x<12:
                self.tab()
                x=x+1
            if not self.find( "titulos_todos_contasReceber", matching=0.97, waiting_time=10000):
                self.not_found("titulos_todos_contasReceber")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()            
            if not self.find( "s_documento_contasReceber", matching=0.97, waiting_time=10000):
                self.not_found("s_documento_contasReceber")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                self.not_found("simexcluirrs")
            self.click()
            self.type_keys_with_interval(1,'movimentacao feita por teste automatico')
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---ADIANTAMENTOS---####
            
            if not self.find( "financeiro", matching=0.97, waiting_time=10000):
                self.not_found("financeiro")
            self.click()
            if not self.find( "adiantamentos", matching=0.97, waiting_time=10000):
                self.not_found("adiantamentos")
            self.click()
            if not self.find( "b_botaobuscar_substituicaoteste", matching=0.97, waiting_time=10000):
                self.not_found("b_botaobuscar_substituicaoteste")
            self.click_relative(80, 122)
            self.enter()
            x=0
            while x<18:
                self.type_down()
                x=x+1
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'8748')
            x=0
            while x<12:
                self.tab()
                x=x+1
            if not self.find( "titulos_todos_contasReceber", matching=0.97, waiting_time=10000):
                self.not_found("titulos_todos_contasReceber")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.wait(500)
            self.type_keys_with_interval(1,'8748')
            self.tab()
            self.tab()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'123')
            if not self.find( "b_cliente_movFinanceiraContasReceber", matching=0.97, waiting_time=10000):
                self.not_found("b_cliente_movFinanceiraContasReceber")
            self.click_relative(211, 158)
            self.wait(500)
            self.enter()
            self.wait(2000)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'12312312312312312312312312312312312312312312')
            self.tab()
            self.type_keys_with_interval(1,'123')
            if not self.find( "b_condPagamento_contasReceber", matching=0.97, waiting_time=10000):
                self.not_found("b_condPagamento_contasReceber")
            self.click_relative(464, 238)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_vendedor_ContasReceber", matching=0.97, waiting_time=10000):
                self.not_found("b_vendedor_ContasReceber")
            self.click_relative(72, 276)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_centroContabilizacao_ContasReceber", matching=0.97, waiting_time=10000):
                self.not_found("b_centroContabilizacao_ContasReceber")
            self.click_relative(495, 276)           
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'te12@!')
            self.tab()
            self.type_keys_with_interval(1,'te12@!')
            if not self.find( "aba1.2.1_ContasReceber", matching=0.97, waiting_time=10000):
                self.not_found("aba1.2.1_ContasReceber")
            self.click()
            if not self.find( "aba1.2.2_ContasReceber", matching=0.97, waiting_time=10000):
                self.not_found("aba1.2.2_ContasReceber")
            self.click()
            if not self.find( "b_classificacao_dadosParcela", matching=0.97, waiting_time=10000):
                self.not_found("b_classificacao_dadosParcela")
            self.click_relative(75, 38)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_planoFinanceiro_ContasReceber", matching=0.97, waiting_time=10000):
                self.not_found("b_planoFinanceiro_ContasReceber")
            self.click_relative(84, 79)
            self.type_keys_with_interval(1,'agua')
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_sacadorAvalista_ContasReceber", matching=0.97, waiting_time=10000):
                self.not_found("b_sacadorAvalista_ContasReceber")
            self.click_relative(75, 116)
            self.enter()
            self.wait(2000)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_contabilancamento_ContasReceber", matching=0.97, waiting_time=10000):
                self.not_found("b_contabilancamento_ContasReceber")
            self.click_relative(475, 40)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_contavilbaixa_ContasReceber", matching=0.97, waiting_time=10000):
                self.not_found("b_contavilbaixa_ContasReceber")
            self.click_relative(473, 76)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_comissao_ContasReceber", matching=0.97, waiting_time=10000):
                self.not_found("b_comissao_ContasReceber")
            self.click_relative(475, 116)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_localCobranca_ContasReceber", matching=0.97, waiting_time=10000):
                self.not_found("b_localCobranca_ContasReceber")
            self.click_relative(875, 37)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_pagamentoPrevisto_ContasReceber", matching=0.97, waiting_time=10000):
                self.not_found("b_pagamentoPrevisto_ContasReceber")
            self.click_relative(876, 76)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_centroCusto_ContasReceber", matching=0.97, waiting_time=10000):
                self.not_found("b_centroCusto_ContasReceber")
            self.click_relative(886, 113)
            self.backspace()
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.backspace()
            self.tab()
            if not self.find( "aba2_contasReceber", matching=0.97, waiting_time=10000):
                self.not_found("aba2_contasReceber")
            self.click()
            if not self.find( "tipolancamento_ContasReceber", matching=0.97, waiting_time=10000):
                self.not_found("tipolancamento_ContasReceber")
            self.double_click_relative(372, 161)
            x=0
            while x<4:
                self.type_down()
                x=x+1
            x=0
            while x<2:
                self.type_down()
                x=x+1
            self.tab()
            x=0
            while x<7:
                self.type_down()
                x=x+1
            if not self.find( "b_propriedade_contasReceber", matching=0.97, waiting_time=10000):
                self.not_found("b_propriedade_contasReceber")
            self.click_relative(74, 212)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.tab()
            self.tab()
            self.space()
            self.space()
            self.tab()
            if not self.find( "aba3_contasReceber", matching=0.97, waiting_time=10000):
                self.not_found("aba3_contasReceber")
            self.click()
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.wait(500)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()      
            self.wait(3000)      
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                self.not_found("simexcluirrs")
            self.click()
            self.type_keys_with_interval(1,'movimentacao feita por teste automatico')
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---CHEQUES RECEBIDOS---####
                             
            if not self.find( "financeiro", matching=0.97, waiting_time=10000):
                self.not_found("financeiro")
            self.click()
            if not self.find( "chequesRecebidos", matching=0.97, waiting_time=10000):
                self.not_found("chequesRecebidos")
            self.click()
            self.enter()
            if not self.find( "aba2_consultadevolucaoitens", matching=0.97, waiting_time=10000):
                self.not_found("aba2_consultadevolucaoitens")
            self.click()
            if not self.find( "b_conta_chequesRecebidos", matching=0.97, waiting_time=10000):
                self.not_found("b_conta_chequesRecebidos")
            self.click_relative(67, 196)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_cliente_chequesRecebidos", matching=0.97, waiting_time=10000):
                self.not_found("b_cliente_chequesRecebidos")
            self.click_relative(70, 237)
            self.enter()
            x=0
            while x<18:
                self.type_down()
                x=x+1
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_localCobranca_chequesRecebidos", matching=0.97, waiting_time=10000):
                self.not_found("b_localCobranca_chequesRecebidos")
            self.click_relative(71, 277)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_banco_chequesRecebidos", matching=0.97, waiting_time=10000):
                self.not_found("b_banco_chequesRecebidos")
            self.click_relative(459, 195)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_clienteNegociado_chequeRecebido", matching=0.97, waiting_time=10000):
                self.not_found("b_clienteNegociado_chequeRecebido")
            self.click_relative(457, 238)
            self.enter()
            x=0
            while x<18:
                self.type_down()
                x=x+1
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_classificacao_chequesRecebidos", matching=0.97, waiting_time=10000):
                self.not_found("b_classificacao_chequesRecebidos")
            self.click_relative(456, 280)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_grupoEmpresa_chequesRecebidos", matching=0.97, waiting_time=10000):
                self.not_found("b_grupoEmpresa_chequesRecebidos")
            self.click_relative(70, 371)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.wait(500)
            self.type_keys_with_interval(1,'8748')
            self.tab()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'123')
            if not self.find( "b_cliente_chequesRecebidos_i", matching=0.97, waiting_time=10000):
                self.not_found("b_cliente_chequesRecebidos_i")
            self.click_relative(77, 163)
            self.enter()
            self.wait(2000)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_banco_chequesRecebidos_i", matching=0.97, waiting_time=10000):
                self.not_found("b_banco_chequesRecebidos_i")
            self.click_relative(490, 163)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'8748')
            self.tab()
            self.type_keys_with_interval(1,'8748')
            if not self.find( "b_localDeCobranca_chequesRecebidos_i", matching=0.97, waiting_time=10000):
                self.not_found("b_localDeCobranca_chequesRecebidos_i")
            self.click_relative(491, 304)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_planoFinanceiro_chequesRecebidos_i", matching=0.97, waiting_time=10000):
                self.not_found("b_planoFinanceiro_chequesRecebidos_i")
            self.click_relative(510, 346)
            self.enter()
            self.type_down()
            self.type_down()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.wait(500)
            if not self.find( "c_periodoEmissao", matching=0.97, waiting_time=10000):
                self.not_found("c_periodoEmissao")
            self.click_relative(314, 80)
            if not self.find( "c_periodoEmissao_carregarDia", matching=0.97, waiting_time=10000):
                self.not_found("c_periodoEmissao_carregarDia")
            self.click()
            if not self.find( "c_periodoEmissao_carregarDia_atual", matching=0.97, waiting_time=10000):
                self.not_found("c_periodoEmissao_carregarDia_atual")
            self.click()            
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()            
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                self.not_found("simexcluirrs")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---MOVIMENTO DE CONTAS---####
                             
            if not self.find( "financeiro", matching=0.97, waiting_time=10000):
                self.not_found("financeiro")
            self.click()
            if not self.find( "movimentoDeContas", matching=0.97, waiting_time=10000):
                self.not_found("movimentoDeContas")
            self.click()
            self.enter()
            if not self.find( "aba2_movFinanceiroContas_selecao", matching=0.97, waiting_time=10000):
                self.not_found("aba2_movFinanceiroContas_selecao")
            self.click()
            if not self.find( "b_cliente_movFinanceiroContas", matching=0.97, waiting_time=10000):
                self.not_found("b_cliente_movFinanceiroContas")
            self.click_relative(69, 179)
            self.enter()   
            self.wait(7000)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(2000)
            if not self.find( "b_grupoEmpresas_movFinanceiroContas", matching=0.97, waiting_time=10000):
                self.not_found("b_grupoEmpresas_movFinanceiroContas")
            self.click_relative(70, 224)
            self.wait(2000)
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "b_classificacao_movFinanceiroContas", matching=0.97, waiting_time=10000):
                self.not_found("b_classificacao_movFinanceiroContas")
            self.click_relative(69, 264)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.backspace()
            self.tab()
            if not self.find( "b_planoFinanceiro_movFinanceiroContas", matching=0.97, waiting_time=10000):
                self.not_found("b_planoFinanceiro_movFinanceiroContas")
            self.click_relative(472, 179)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_tipoPagamento_movFinanceiroContas", matching=0.97, waiting_time=10000):
                self.not_found("b_tipoPagamento_movFinanceiroContas")
            self.click_relative(472, 263)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.backspace()
            self.tab()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.wait(500)
            self.type_keys_with_interval(1,'8748')
            self.tab()
            self.tab()
            self.tab()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            if not self.find( "b_conta_cadMovConta", matching=0.97, waiting_time=10000):
                self.not_found("b_conta_cadMovConta")
            self.click_relative(536, 137)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_tipoPagamento_cadMovConta", matching=0.97, waiting_time=10000):
                self.not_found("b_tipoPagamento_cadMovConta")
            self.click_relative(976, 136)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_fornecedor_cadMovConta", matching=0.97, waiting_time=10000):
                self.not_found("b_fornecedor_cadMovConta")
            self.click_relative(422, 174)
            self.enter()
            self.wait(7000)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_planoFinanceiro_cadMovConta", matching=0.97, waiting_time=10000):
                self.not_found("b_planoFinanceiro_cadMovConta")
            self.click_relative(92, 219)
            self.enter()
            self.type_down()
            self.type_down()
            self.type_down()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_operacao_cadMovConta", matching=0.97, waiting_time=10000):
                self.not_found("b_operacao_cadMovConta")
            self.click_relative(971, 222)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_centroDeCustos_cadMovConta", matching=0.97, waiting_time=10000):
                self.not_found("b_centroDeCustos_cadMovConta")
            self.click_relative(535, 260)
            self.backspace()
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.backspace()
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.wait(500)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()            
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                self.not_found("simexcluirrs")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.wait(2000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---RECIBO AVULSO---####
                             
            if not self.find( "financeiro", matching=0.97, waiting_time=10000):
                self.not_found("financeiro")
            self.click()
            if not self.find( "reciboavulso", matching=0.97, waiting_time=10000):
                self.not_found("reciboavulso")
            self.click()
            if not self.find( "b_empresa_reciboAvulso", matching=0.97, waiting_time=10000):
                self.not_found("b_empresa_reciboAvulso")
            self.click_relative(168, 97)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_clienteFornecedor_reciboAvulso", matching=0.97, waiting_time=10000):
                self.not_found("b_clienteFornecedor_reciboAvulso")
            self.click_relative(167, 124)
            self.enter()
            x=0
            while x<18:
                self.type_down()
                x=x+1
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            x=0
            while x<11:
                self.tab()
                x=x+1
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.tab()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'8748')
            self.tab()
            self.type_down()
            self.type_up()
            self.tab()
            self.type_keys_with_interval(1,'123')
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---ENCONTRO DE CONTAS---####
                             
            if not self.find( "financeiro", matching=0.97, waiting_time=10000):
                self.not_found("financeiro")
            self.click()                 
            if not self.find( "encontrodecontas", matching=0.97, waiting_time=10000):
                self.not_found("encontrodecontas")
            self.click()
            if not self.find( "b_clienteFornecedor_encontroDeContas", matching=0.97, waiting_time=10000):
                self.not_found("b_clienteFornecedor_encontroDeContas")
            self.click_relative(68, 109)
            self.wait(500)
            self.enter()
            x=0
            while x<18:
                self.type_down()
                x=x+1
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "aba2_encontroDeContas", matching=0.97, waiting_time=10000):
                self.not_found("aba2_encontroDeContas")
            self.click()
            if not self.find( "b_grupoDeEmpresas_encontroDeContas", matching=0.97, waiting_time=10000):
                self.not_found("b_grupoDeEmpresas_encontroDeContas")
            self.click_relative(70, 147)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.wait(2000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---ORÇADO X REALIZADO---####
                             
            if not self.find( "financeiro", matching=0.97, waiting_time=10000):
                self.not_found("financeiro")
            self.click() 
            if not self.find( "orcadoxrealizado", matching=0.97, waiting_time=10000):
                self.not_found("orcadoxrealizado")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.enter()
            if not self.find( "b_planoFinanceiro_conOrcadoXRealizado", matching=0.97, waiting_time=10000):
                self.not_found("b_planoFinanceiro_conOrcadoXRealizado")
            self.click_relative(330, 79)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.wait(500)
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "b_aba3_planoFinanceiro_orcadoXRealizado", matching=0.97, waiting_time=10000):
                self.not_found("b_aba3_planoFinanceiro_orcadoXRealizado")
            self.click_relative(92, 219)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.enter()
            if not self.find( "aba4_conOrcadoXRealizado", matching=0.97, waiting_time=10000):
                self.not_found("aba4_conOrcadoXRealizado")
            self.click()
            if not self.find( "aba2_OrcadoXRealizado", matching=0.97, waiting_time=10000):
                self.not_found("aba2_OrcadoXRealizado")
            self.click()
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.wait(500)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()            
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                self.not_found("simexcluirrs")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.enter()
            self.wait(2000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---MOV. FRENTE DE CAIXA---####
                             
            if not self.find( "financeiro", matching=0.97, waiting_time=10000):
                self.not_found("financeiro")
            self.click() 
            if not self.find( "movFrenteDeCaixa", matching=0.97, waiting_time=10000):
                self.not_found("movFrenteDeCaixa")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "b_cliente_movCaixa", matching=0.97, waiting_time=10000):
                self.not_found("b_cliente_movCaixa")
            self.click_relative(306, 84)
            self.enter()
            x=0
            while x<18:
                self.type_down()
                x=x+1
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "aba3_movCaixa", matching=0.97, waiting_time=10000):
                self.not_found("aba3_movCaixa")
            self.click()
            if not self.find( "b_tipoPagamento_movCaixa", matching=0.97, waiting_time=10000):
                self.not_found("b_tipoPagamento_movCaixa")
            self.click_relative(51, 151)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---REMESSA BANCARIA RECEB---####
                             
            if not self.find( "financeiro", matching=0.97, waiting_time=10000):
                self.not_found("financeiro")
            self.click() 
            if not self.find( "remessabancaria", matching=0.97, waiting_time=10000):
                self.not_found("remessabancaria")
            self.click()
            if not self.find( "localizar_fonte_receb", matching=0.97, waiting_time=10000):
                self.not_found("localizar_fonte_receb")
            self.click()            
            self.type_right()
            self.enter()
            if not self.find( "aba5_receb", matching=0.97, waiting_time=10000):
                self.not_found("aba5_receb")
            self.click()
            if not self.find( "b_cliente_PIXGeracao", matching=0.97, waiting_time=10000):
                self.not_found("b_cliente_PIXGeracao")
            self.click_relative(72, 185)
            self.enter()
            while x<18:
                self.type_down()
                x=x+1
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_classificacao_PIXGeracao", matching=0.97, waiting_time=10000):
                self.not_found("b_classificacao_PIXGeracao")
            self.click_relative(75, 229)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_LocalCobranca_PIXGeracao", matching=0.97, waiting_time=10000):
                self.not_found("b_LocalCobranca_PIXGeracao")
            self.click_relative(75, 274)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_condicaoPagamento_PIXGeracao", matching=0.97, waiting_time=10000):
                self.not_found("b_condicaoPagamento_PIXGeracao")
            self.click_relative(74, 324)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_vendedor_PIXGeracao", matching=0.97, waiting_time=10000):
                self.not_found("b_vendedor_PIXGeracao")
            self.click_relative(521, 184)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_planoFinanceiro_PIXGeracao", matching=0.97, waiting_time=10000):
                self.not_found("b_planoFinanceiro_PIXGeracao")
            self.click_relative(531, 230)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_tipoPagamento_PIXGeracao", matching=0.97, waiting_time=10000):
                self.not_found("b_tipoPagamento_PIXGeracao")
            self.click_relative(523, 274)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_grupoEmpresas_PIXGeracao", matching=0.97, waiting_time=10000):
                self.not_found("b_grupoEmpresas_PIXGeracao")
            self.click_relative(524, 323)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            if not self.find( "aba2_remessaReceb", matching=0.97, waiting_time=10000):
                self.not_found("aba2_remessaReceb")
            self.click()
            if not self.find( "b_operacaoBaixa_testeSubstituicao", matching=0.97, waiting_time=10000):
                self.not_found("b_operacaoBaixa_testeSubstituicao")
            self.click_relative(768, 219)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_tipoPagamento_testeSubstituicao", matching=0.97, waiting_time=10000):
               self.not_found("b_tipoPagamento_testeSubstituicao")
            self.click_relative(68, 223)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "fonte_retornar_remessaReceb", matching=0.97, waiting_time=10000):
                self.not_found("fonte_retornar_remessaReceb")
            self.click()
            
                            ####---REMESSA BANCARIA RECEB API---####
                             
            if not self.find( "financeiro", matching=0.97, waiting_time=10000):
                self.not_found("financeiro")
            self.click() 
            if not self.find( "remessaRecebAPI", matching=0.97, waiting_time=10000):
                self.not_found("remessaRecebAPI")
            self.click()
            if not self.find( "localizar_fonte_receb", matching=0.97, waiting_time=10000):
                self.not_found("localizar_fonte_receb")
            self.click()            
            self.type_right()
            self.enter()
            if not self.find( "aba5_receb", matching=0.97, waiting_time=10000):
                self.not_found("aba5_receb")
            self.click()
            if not self.find( "b_cliente_remessaRecebAPI", matching=0.97, waiting_time=10000):
                self.not_found("b_cliente_remessaRecebAPI")
            self.click_relative(94, 249)
            self.enter()
            x=0
            while x<18:
                self.type_down()
                x=x+1
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_classificacao_remessaRecebAPI", matching=0.97, waiting_time=10000):
                self.not_found("b_classificacao_remessaRecebAPI")
            self.click_relative(94, 295)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_localCobranca_remessaRecebAPI", matching=0.97, waiting_time=10000):
                self.not_found("b_localCobranca_remessaRecebAPI")
            self.click_relative(94, 343)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_condPagamento_remessaRecebAPI", matching=0.97, waiting_time=10000):
                self.not_found("b_condPagamento_remessaRecebAPI")
            self.click_relative(94, 386)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_vendedor_remessaRecebAPI", matching=0.97, waiting_time=10000):
                self.not_found("b_vendedor_remessaRecebAPI")
            self.click_relative(544, 250)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_planoFinanceiro_remessaRecebAPI", matching=0.97, waiting_time=10000):
                self.not_found("b_planoFinanceiro_remessaRecebAPI")
            self.click_relative(548, 297)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_tipoPagamento_remessaRecebAPI", matching=0.97, waiting_time=10000):
                self.not_found("b_tipoPagamento_remessaRecebAPI")
            self.click_relative(539, 341)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_grupoEmpresa_remessaRecebAPI", matching=0.97, waiting_time=10000):
                self.not_found("b_grupoEmpresa_remessaRecebAPI")
            self.click_relative(544, 388)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            if not self.find( "aba2_remessaReceb", matching=0.97, waiting_time=10000):
                self.not_found("aba2_remessaReceb")
            self.click()
            if not self.find( "b2_tipoPagamento_remessaRecebAPI", matching=0.97, waiting_time=10000):
                self.not_found("b2_tipoPagamento_remessaRecebAPI")
            self.click_relative(66, 243)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b2_centroCusto_remessaRecebAPI", matching=0.97, waiting_time=10000):
                self.not_found("b2_centroCusto_remessaRecebAPI")
            self.click_relative(108, 292)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_tipoPagamento_remessaRecebAPI", matching=0.97, waiting_time=10000):
                self.not_found("b_tipoPagamento_remessaRecebAPI")
            self.click_relative(67, 341)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_operacaoBaixa_remessaRecebAPI", matching=0.97, waiting_time=10000):
                self.not_found("b_operacaoBaixa_remessaRecebAPI")
            self.click_relative(787, 243)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "fonte_retornar_remessaReceb", matching=0.97, waiting_time=10000):
                self.not_found("fonte_retornar_remessaReceb")
            self.click()
            
                            ####---REMESSA BANCARIA PAGAMENTO---####
                             
            if not self.find( "financeiro", matching=0.97, waiting_time=10000):
                self.not_found("financeiro")
            self.click() 
            if not self.find( "remessabancariapagamento", matching=0.97, waiting_time=10000):
                self.not_found("remessabancariapagamento")
            self.click()
            if not self.find( "aba5_receb", matching=0.97, waiting_time=10000):
                self.not_found("aba5_receb")
            self.click()
            if not self.find( "b_cliente_remessaPaga", matching=0.97, waiting_time=10000):
                self.not_found("b_cliente_remessaPaga")
            self.click_relative(95, 277)
            self.enter()
            x=0
            while x<18:
                self.type_down()
                x=x+1
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_planoFinanceiro_remessaPaga", matching=0.97, waiting_time=10000):
                self.not_found("b_planoFinanceiro_remessaPaga")
            self.click_relative(97, 324)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_classificacao_remessaPaga", matching=0.97, waiting_time=10000):
                self.not_found("b_classificacao_remessaPaga")
            self.click_relative(97, 365)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_localCobranca_remessaPaga", matching=0.97, waiting_time=10000):
                self.not_found("b_localCobranca_remessaPaga")
            self.click_relative(94, 410)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_tipoPagamento_remessaPaga", matching=0.97, waiting_time=10000):
                self.not_found("b_tipoPagamento_remessaPaga")
            self.click_relative(475, 320)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_condPagamento_remessaPaga", matching=0.97, waiting_time=10000):
                self.not_found("b_condPagamento_remessaPaga")
            self.click_relative(474, 365)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.wait(2000)
            self.enter()
            self.type_down()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.wait(2000)
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---REMESSA SERASA---####
                             
            if not self.find( "financeiro", matching=0.97, waiting_time=10000):
                self.not_found("financeiro")
            self.click() 
            if not self.find( "remessaserasa", matching=0.97, waiting_time=10000):
                self.not_found("remessaserasa")
            self.click()
            if not self.find( "aba5_receb", matching=0.97, waiting_time=10000):
                self.not_found("aba5_receb")
            self.click()
            if not self.find( "b_cliente_gerSerasa", matching=0.97, waiting_time=10000):
                self.not_found("b_cliente_gerSerasa")
            self.click_relative(84, 203)
            self.enter()
            x=0
            while x<18:
                self.type_down()
                x=x+1
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_planoFinanceiro_gerSerasa", matching=0.97, waiting_time=10000):
                self.not_found("b_planoFinanceiro_gerSerasa")
            self.click_relative(96, 293)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_classificacao_gerSerasa", matching=0.97, waiting_time=10000):
                self.not_found("b_classificacao_gerSerasa")
            self.click_relative(97, 338)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_localCobranca_gerSerasa", matching=0.97, waiting_time=10000):
                self.not_found("b_localCobranca_gerSerasa")
            self.click_relative(95, 381)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_grupoEmpresa_gerSerasa", matching=0.97, waiting_time=10000):
                self.not_found("b_grupoEmpresa_gerSerasa")
            self.click_relative(96, 423)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            self.backspace()
            self.tab()
            if not self.find( "b_tipoPagamento_gerSerasa", matching=0.97, waiting_time=10000):
                self.not_found("b_tipoPagamento_gerSerasa")
            self.click_relative(475, 292)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_vendedor_gerSerasa", matching=0.97, waiting_time=10000):
                self.not_found("b_vendedor_gerSerasa")
            self.click_relative(474, 336)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_condPagamento_gerSerasa", matching=0.97, waiting_time=10000):
                self.not_found("b_condPagamento_gerSerasa")
            self.click_relative(474, 382)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.wait(2000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---MOVIMENTO TESOURARIA---####
                             
            if not self.find( "financeiro", matching=0.97, waiting_time=10000):
                self.not_found("financeiro")
            self.click() 
            if not self.find( "movimentoTesouraria", matching=0.97, waiting_time=10000):
                self.not_found("movimentoTesouraria")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.wait(2000)
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.wait(500)
            self.type_keys_with_interval(1,'123')
            if not self.find( "ir_movTesouraria", matching=0.97, waiting_time=10000):
                self.not_found("ir_movTesouraria")
            self.click_relative(13, 136)
            if not self.find( "b_ir_ECF_movTesouraria", matching=0.97, waiting_time=10000):
                self.not_found("b_ir_ECF_movTesouraria")
            self.click_relative(75, 150)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_ir_tipoRecebimento_movTesouraria", matching=0.97, waiting_time=10000):
                self.not_found("b_ir_tipoRecebimento_movTesouraria")
            self.click_relative(73, 189)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.enter()
            self.enter()
            self.type_right()
            self.enter()
            if not self.find( "cancelar_movTesouraria", matching=0.97, waiting_time=10000):
                self.not_found("cancelar_movTesouraria")
            self.click_relative(333, 35)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---EXPORTACOES EMPORIUM BALANCA---####
                             
            if not self.find( "comunicacao", matching=0.97, waiting_time=10000):
                self.not_found("comunicacao")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "exportacaoEmporium", matching=0.97, waiting_time=10000):
                self.not_found("exportacaoEmporium")
            self.click()
            if not self.find( "balancas_impEmp", matching=0.97, waiting_time=10000):
                self.not_found("balancas_impEmp")
            self.click()
            self.tab()
            self.type_right()
            self.type_right()
            self.type_right()
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_right()
            self.tab()
            self.type_right()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---FRENTE DE CAIXA---####
                             
            if not self.find( "comunicacao", matching=0.97, waiting_time=10000):
                self.not_found("comunicacao")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "exportacaoEmporium", matching=0.97, waiting_time=10000):
                self.not_found("exportacaoEmporium")
            self.click()
            if not self.find( "frenteDeCaixa", matching=0.97, waiting_time=10000):
                self.not_found("frenteDeCaixa")
            self.click()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.tab()
            self.type_left()
            self.type_right()
            self.type_right()
            self.tab()
            self.type_left()
            self.type_left()
            self.tab()
            self.type_right()
            self.type_left()
            self.type_left()
            self.type_left()
            self.type_left()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---COLETOR DE DADOS---####
                             
            if not self.find( "comunicacao", matching=0.97, waiting_time=10000):
                self.not_found("comunicacao")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "exportacaoEmporium", matching=0.97, waiting_time=10000):
                self.not_found("exportacaoEmporium")
            self.click()
            if not self.find( "coletorDeDados", matching=0.97, waiting_time=10000):
                self.not_found("coletorDeDados")
            self.click()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.tab()
            self.type_right()
            self.tab()
            self.type_right()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
            
                            ####---TERMINAL DE CONSULTA---####
                             
            if not self.find( "comunicacao", matching=0.97, waiting_time=10000):
                self.not_found("comunicacao")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "exportacaoEmporium", matching=0.97, waiting_time=10000):
                self.not_found("exportacaoEmporium")
            self.click()
            if not self.find( "terminalDeConsulta", matching=0.97, waiting_time=10000):
                self.not_found("terminalDeConsulta")
            self.click()
            self.type_right()
            self.tab()
            while x<9:
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                x=x+1
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()

                            ####---ITENS PITÁGORAS---####

            if not self.find( "comunicacao", matching=0.97, waiting_time=10000):
                self.not_found("comunicacao")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "exportacaoEmporium", matching=0.97, waiting_time=10000):
                self.not_found("exportacaoEmporium")
            self.click()
            if not self.find( "itensPitagoras", matching=0.97, waiting_time=10000):
                self.not_found("itensPitagoras")
            self.click()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---PEDIDOS DE VENDA---####
                             
            if not self.find( "comunicacao", matching=0.97, waiting_time=10000):
                self.not_found("comunicacao")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "exportacaoEmporium", matching=0.97, waiting_time=10000):
                self.not_found("exportacaoEmporium")
            self.click()
            if not self.find( "pedidosDeVenda", matching=0.97, waiting_time=10000):
                self.not_found("pedidosDeVenda")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.enter()
            self.type_keys_with_interval(1,'01012000')
            self.tab()
            self.tab()
            self.type_right()
            self.type_right()
            self.type_left()
            self.type_left()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---CAMPANHAS---####
                             
            if not self.find( "comunicacao", matching=0.97, waiting_time=10000):
                self.not_found("comunicacao")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "exportacaoEmporium", matching=0.97, waiting_time=10000):
                self.not_found("exportacaoEmporium")
            self.click()
            if not self.find( "campanhas_comunicacoes", matching=0.97, waiting_time=10000):
                self.not_found("campanhas_comunicacoes")
            self.click()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.tab()
            self.space()
            self.space()
            self.tab()
            self.space()
            self.space()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---EDI NESTLE---####
            
            if not self.find( "comunicacao", matching=0.97, waiting_time=10000):
                self.not_found("comunicacao")
            self.click()
            if not self.find( "EDINestle", matching=0.97, waiting_time=10000):
                self.not_found("EDINestle")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.enter()
            self.tab()
            self.tab()
            self.tab()
            self.tab()
            x=0
            while x<6:
                self.space()
                self.space()
                self.tab()
                x=x+1
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---IMPORTACAO XML---####
                             
            if not self.find( "comunicacao", matching=0.97, waiting_time=10000):
                self.not_found("comunicacao")
            self.click()
            if not self.find( "importacaoXML", matching=0.97, waiting_time=10000):
                self.not_found("importacaoXML")
            self.click()
            if not self.find( "b_CFOPadrao_impXML", matching=0.97, waiting_time=10000):
                self.not_found("b_CFOPadrao_impXML")
            self.click_relative(551, 98)
            self.type_down()
            self.enter()
            if not self.find( "b_operacaoPadrao_impXML", matching=0.97, waiting_time=10000):
                self.not_found("b_operacaoPadrao_impXML")
            self.click_relative(552, 118)
            self.type_down()
            self.enter()
            if not self.find( "b_grupoFiscal_impXML", matching=0.97, waiting_time=10000):
                self.not_found("b_grupoFiscal_impXML")
            self.click_relative(549, 138)
            self.type_down()
            self.enter()
            if not self.find( "b_clienteFornecedor_impXML", matching=0.97, waiting_time=10000):
                self.not_found("b_clienteFornecedor_impXML")
            self.click_relative(1011, 198)
            x=0
            while x<18:
                self.type_down()
                x=x+1
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---VENDAS E COMPRAS MVTO---####
                             
            if not self.find( "consultas", matching=0.97, waiting_time=10000):
                self.not_found("consultas")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "vendasECompras", matching=0.97, waiting_time=10000):
                self.not_found("vendasECompras")
            self.click()
            if not self.find( "aba3_selecao_MVC", matching=0.97, waiting_time=10000):
                self.not_found("aba3_selecao_MVC")
            self.click()
            if not self.find( "b_clienteFornecedor_MVC", matching=0.97, waiting_time=10000):
                self.not_found("b_clienteFornecedor_MVC")
            self.click_relative(71, 163)
            self.enter()
            x=0
            while x<18:
                self.type_down()
                x=x+1
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.backspace()
            self.tab()
            if not self.find( "b_condicaoPagamento_MVC", matching=0.97, waiting_time=10000):
                self.not_found("b_condicaoPagamento_MVC")
            self.click_relative(70, 203)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.backspace()
            self.tab()
            if not self.find( "b_vendedorComprador_MVC", matching=0.97, waiting_time=10000):
                self.not_found("b_vendedorComprador_MVC")
            self.click_relative(453, 161)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.backspace()
            self.tab()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---CONSULTAS ORDEM DE SERVICO---####
                             
            if not self.find( "consultas", matching=0.97, waiting_time=10000):
                self.not_found("consultas")
            self.click()
            if not self.find( "ordemDeServico_consulta", matching=0.97, waiting_time=10000):
                self.not_found("ordemDeServico_consulta")
            self.click()
            if not self.find( "aba4_selecao_COS", matching=0.97, waiting_time=10000):
                self.not_found("aba4_selecao_COS")
            self.click()
            if not self.find( "b_condPag_COS", matching=0.97, waiting_time=10000):
                self.not_found("b_condPag_COS")
            self.click_relative(73, 193)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_recepcionista_COS", matching=0.97, waiting_time=10000):
                self.not_found("b_recepcionista_COS")
            self.click_relative(464, 196)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_executor_COS", matching=0.97, waiting_time=10000):
                self.not_found("b_executor_COS")
            self.click_relative(72, 238)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_servico_COS", matching=0.97, waiting_time=10000):
                self.not_found("b_servico_COS")
            self.click_relative(462, 240)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            self.backspace()
            self.tab()
            if not self.find( "b_tipoOS_COS", matching=0.97, waiting_time=10000):
                self.not_found("b_tipoOS_COS")
            self.click_relative(73, 286)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.enter()
            if not self.find( "b_cliente_COS", matching=0.97, waiting_time=10000):
                self.not_found("b_cliente_COS")
            self.click_relative(633, 125)
            self.enter()
            self.wait(500)
            x=0
            while x<18:
                self.type_down()
                x=x+1
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---CURVAS A, B, C---####
                             
            if not self.find( "consultas", matching=0.97, waiting_time=10000):
                self.not_found("consultas")
            self.click()
            if not self.find( "curvasabc_consultas", matching=0.97, waiting_time=10000):
                self.not_found("curvasabc_consultas")
            self.click()
            self.tab()
            self.tab()
            self.type_up()
            self.type_down()
            self.tab()
            self.type_up()
            self.type_down()
            self.tab()
            self.type_up()
            self.type_down()
            self.tab()
            self.tab()
            self.tab()
            self.space()
            self.space()
            self.tab()
            self.space()
            self.space()
            self.tab()
            self.type_up()
            self.type_down()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---GIRO E LUCRATIVIDADE---####
                             
            if not self.find( "consultas", matching=0.97, waiting_time=10000):
                self.not_found("consultas")
            self.click()
            if not self.find( "giroELucratividade", matching=0.97, waiting_time=10000):
                self.not_found("giroELucratividade")
            self.click()
            if not self.find( "b_fornecedor_CGL", matching=0.97, waiting_time=10000):
                self.not_found("b_fornecedor_CGL")
            self.click_relative(310, 83)
            self.wait(500)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.tab()
            self.tab()
            x=0
            while x<6:
                self.type_down()
                x=x+1
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---VENDAS X COMPRAS---####
                             
            if not self.find( "consultas", matching=0.97, waiting_time=10000):
                self.not_found("consultas")
            self.click()
            if not self.find( "vendasXCompras", matching=0.97, waiting_time=10000):
                self.not_found("vendasXCompras")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---CONSULTA FATURAMENTO---####
                             
            if not self.find( "consultas", matching=0.97, waiting_time=10000):
                self.not_found("consultas")
            self.click()
            if not self.find( "consultaFaturamento", matching=0.97, waiting_time=10000):
                self.not_found("consultaFaturamento")
            self.click()
            if not self.find( "a2_consultaFaturamento", matching=0.97, waiting_time=10000):
                self.not_found("a2_consultaFaturamento")
            self.click()           
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---COMPRAS EFETIVAS---####
            
            if not self.find( "consultas", matching=0.97, waiting_time=10000):
                self.not_found("consultas")
            self.click()
            if not self.find( "consultaComprasEfetivas", matching=0.97, waiting_time=10000):
                self.not_found("consultaComprasEfetivas")
            self.click()
            if not self.find( "a2_consultaFaturamento", matching=0.97, waiting_time=10000):
                self.not_found("a2_consultaFaturamento")
            self.click()      
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---COMPRA DE ITENS---####
                             
            if not self.find( "consultas", matching=0.97, waiting_time=10000):
                self.not_found("consultas")
            self.click()
            if not self.find( "consulta_CompraItens", matching=0.97, waiting_time=10000):
                self.not_found("consulta_CompraItens")
            self.click()
            if not self.find( "consultar", matching=0.97, waiting_time=10000):
                self.not_found("consultar")
            self.click()
            if not self.find( "b_selecao_consultaCompraItens", matching=0.97, waiting_time=10000):
                self.not_found("b_selecao_consultaCompraItens")
            self.click_relative(70, 84)
            self.enter()
            self.wait(500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "consultar", matching=0.97, waiting_time=10000):
                self.not_found("consultar")
            self.click()
            self.backspace()
            self.tab()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.wait(500)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---CONSULTA FINANCEIRO---####
                             
            if not self.find( "consultas", matching=0.97, waiting_time=10000):
                self.not_found("consultas")
            self.click()
            if not self.find( "consulta_financeiro", matching=0.97, waiting_time=10000):
                self.not_found("consulta_financeiro")
            self.click()
            if not self.find( "p_vencimento_CMF", matching=0.97, waiting_time=10000):
                self.not_found("p_vencimento_CMF")
            self.click_relative(1317, 123)
            if not self.find( "carregar_ano", matching=0.97, waiting_time=10000):
                self.not_found("carregar_ano")
            self.click()
            if not self.find( "carregar_ano_anterior", matching=0.97, waiting_time=10000):
                self.not_found("carregar_ano_anterior")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.wait(2000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---HISTORICO DE CLIENTES---####
                             
            if not self.find( "consultas", matching=0.97, waiting_time=10000):
                self.not_found("consultas")
            self.click()
            if not self.find( "historicoDeClientes", matching=0.97, waiting_time=10000):
                self.not_found("historicoDeClientes")
            self.click()
            if not self.find( "b_cliente_historicoCliente", matching=0.97, waiting_time=10000):
                self.not_found("b_cliente_historicoCliente")
            self.click_relative(67, 83)
            self.enter()
            x=0
            while x<18:
                self.type_down()
                x=x+1
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(1500)
            if not self.find( "a2_CHC", matching=0.97, waiting_time=10000):
                self.not_found("a2_CHC")
            self.click()
            if not self.find( "a2p3_CHC", matching=0.97, waiting_time=10000):
                self.not_found("a2p3_CHC")
            self.click()
            if not self.find( "b_conta_a2p3_CHC", matching=0.97, waiting_time=10000):
                self.not_found("b_conta_a2p3_CHC")
            self.click_relative(74, 170)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.wait(2000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---METAS DE VENDEDORES---####
                             
            if not self.find( "consultas", matching=0.97, waiting_time=10000):
                self.not_found("consultas")
            self.click()
            if not self.find( "metasDeVendedores", matching=0.97, waiting_time=10000):
                self.not_found("metasDeVendedores")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.wait(2000)
            self.enter()
            if not self.find( "a2_consultaFaturamento", matching=0.97, waiting_time=10000):
                self.not_found("a2_consultaFaturamento")
            self.click()  
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.wait(2000)
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---LIMITE COMPRA VENDEDORES---####
                             
            if not self.find( "consultas", matching=0.97, waiting_time=10000):
                self.not_found("consultas")
            self.click()
            if not self.find( "limiteCompraVendedores", matching=0.97, waiting_time=10000):
                self.not_found("limiteCompraVendedores")
            self.click()
            x=0
            while x<12:
                self.type_down()
                x=x+1
            self.tab()
            self.type_up()
            self.type_down()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.wait(2000)
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---CHECAGEM NFE---####
                             
            if not self.find( "consultas", matching=0.97, waiting_time=10000):
                self.not_found("consultas")
            self.click()
            if not self.find( "checagemNFE", matching=0.97, waiting_time=10000):
                self.not_found("checagemNFE")
            self.click()
            if not self.find( "checagem_CNFE", matching=0.97, waiting_time=10000):
                self.not_found("checagem_CNFE")
            self.click()
            self.wait(180000)
            #if not self.find( "cod_guarapuava_checagemNFE", matching=0.97, waiting_time=100000):
            #    self.not_found("cod_guarapuava_checagemNFE")
            #self.click()
            if not self.find( "cod_0109_guarapuava_checagem", matching=0.97, waiting_time=10000):
                self.not_found("cod_0109_guarapuava_checagem")
            self.click()
            self.wait(7000)          
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
               self.not_found("retornarpe")
            self.click()
            
                            ####---APONTAMENTOS DE SERVICOS---####
                             
            if not self.find( "consultas", matching=0.97, waiting_time=10000):
                self.not_found("consultas")
            self.click()
            if not self.find( "apontamentosDeServicos", matching=0.97, waiting_time=10000):
                self.not_found("apontamentosDeServicos")
            self.click()
            if not self.find( "a2_consultaFaturamento", matching=0.97, waiting_time=10000):
                self.not_found("a2_consultaFaturamento")
            self.click()  
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "aba_cliente_ConsultaAp", matching=0.97, waiting_time=10000):
                self.not_found("aba_cliente_ConsultaAp")
            self.click()
            if not self.find( "b_cliente_ConsultaAp", matching=0.97, waiting_time=10000):
                self.not_found("b_cliente_ConsultaAp")
            self.click_relative(656, 93)
            self.enter()
            self.wait(500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_up()
            x=0
            while x<3:
                self.type_down()
                x=x+1
            if not self.find( "b_servico_CadApontamento", matching=0.97, waiting_time=10000):
                self.not_found("b_servico_CadApontamento")
            self.click_relative(607, 110)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_executor_CadApontamento", matching=0.97, waiting_time=10000):
                self.not_found("b_executor_CadApontamento")
            self.click_relative(610, 182)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_motivoSaida_CadApontamento", matching=0.97, waiting_time=10000):
                self.not_found("b_motivoSaida_CadApontamento")
            self.click_relative(604, 300)
            if not self.find( "cancelar_cadApontamento", matching=0.97, waiting_time=10000):
                self.not_found("cancelar_cadApontamento")
            self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
               self.not_found("retornarpe")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
               self.not_found("retornarpe")
            self.click()
            
                            ####---EMAILS ENVIADOS---####
                             
            if not self.find( "consultas", matching=0.97, waiting_time=10000):
                self.not_found("consultas")
            self.click()
            if not self.find( "emailsEnviados", matching=0.97, waiting_time=10000):
                self.not_found("emailsEnviados")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.wait(2000)
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---HISTORICO DE ITENS---####
                             
            if not self.find( "consultas", matching=0.97, waiting_time=10000):
                self.not_found("consultas")
            self.click()
            if not self.find( "historicoDeItens", matching=0.97, waiting_time=10000):
                self.not_found("historicoDeItens")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.wait(2000)
            if not self.find( "a9_HistoricoItem", matching=0.97, waiting_time=10000):
                self.not_found("a9_HistoricoItem")
            self.double_click()
            if not self.find( "a9_historicoItens_marcado", matching=0.97, waiting_time=10000):
                self.not_found("a9_historicoItens_marcado")
            self.click()
            self.tab()
            self.type_keys_with_interval(1,'8748')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            x=0
            while x<11:
                self.type_down()
                x=x+1
            if not self.find( "b_localEstoque_historicoItem", matching=0.97, waiting_time=10000):
                self.not_found("b_localEstoque_historicoItem")
            self.click_relative(639, 242)
            self.wait(1000)
            if not self.find( "selecionarpe", matching=0.97, waiting_time=10000):
                self.not_found("selecionarpe")
            self.click()
            self.wait(500)
            self.enter()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.wait(2000)
            #self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.wait(500)
            #if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
            #    self.not_found("retornarpe")
            #self.click()
            
                            ####---GRAFICOS VENDAS POR PERIODO---####
                             
            if not self.find( "graficos2", matching=0.97, waiting_time=10000):
                self.not_found("graficos2")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "vendasPorPeriodo", matching=0.97, waiting_time=10000):
                self.not_found("vendasPorPeriodo")
            self.click()
            if not self.find( "data", matching=0.97, waiting_time=10000):
                self.not_found("data")
            self.click_relative(33, 7)
            if not self.find( "data_ano", matching=0.97, waiting_time=10000):
                self.not_found("data_ano")
            self.click()
            if not self.find( "data_ano_anterior", matching=0.97, waiting_time=10000):
                self.not_found("data_ano_anterior")
            self.click()
            if not self.find( "gerarGrafico", matching=0.97, waiting_time=10000):
                self.not_found("gerarGrafico")
            self.click()
            self.wait(10000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---ITENS VENDIDOS NO PERIODO---####
                             
            if not self.find( "graficos2", matching=0.97, waiting_time=10000):
                self.not_found("graficos2")
            self.click()
            if not self.find( "itensVendidosPeriodo", matching=0.97, waiting_time=10000):
                self.not_found("itensVendidosPeriodo")
            self.click()
            if not self.find( "data", matching=0.97, waiting_time=10000):
                self.not_found("data")
            self.click_relative(33, 7)
            if not self.find( "data_ano", matching=0.97, waiting_time=10000):
                self.not_found("data_ano")
            self.click()
            if not self.find( "data_ano_anterior", matching=0.97, waiting_time=10000):
                self.not_found("data_ano_anterior")
            self.click()
            if not self.find( "gerarGrafico", matching=0.97, waiting_time=10000):
                self.not_found("gerarGrafico")
            self.click()
            self.wait(15000)
            #if not self.find( "escala_gráfico_itensMaisVendidos", matching=0.97, waiting_time=10000):
            #    self.not_found("escala_gráfico_itensMaisVendidos")         
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.wait(1500)
            
                            ####---TOTAL DE VENDAS POR CLIENTE---####

            self.wait(1500)                 
            if not self.find( "graficos2", matching=0.97, waiting_time=10000):
                self.not_found("graficos2")
            self.click()
            if not self.find( "totalVendasPorCliente", matching=0.97, waiting_time=10000):
                self.not_found("totalVendasPorCliente")
            self.click()
            if not self.find( "data", matching=0.97, waiting_time=10000):
                self.not_found("data")
            self.click_relative(33, 7)
            if not self.find( "data_ano", matching=0.97, waiting_time=10000):
                self.not_found("data_ano")
            self.click()
            if not self.find( "data_ano_anterior", matching=0.97, waiting_time=10000):
                self.not_found("data_ano_anterior")
            self.click()
            if not self.find( "gerarGrafico", matching=0.97, waiting_time=10000):
                self.not_found("gerarGrafico")
            self.click()
            self.wait(10000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---COMPRAS POR PERIODO---####
                             
            if not self.find( "graficos2", matching=0.97, waiting_time=10000):
                self.not_found("graficos2")
            self.click()
            if not self.find( "comprasPorPeriodo", matching=0.97, waiting_time=10000):
                self.not_found("comprasPorPeriodo")
            self.click()
            if not self.find( "data", matching=0.97, waiting_time=10000):
                self.not_found("data")
            self.click_relative(33, 7)
            if not self.find( "data_ano", matching=0.97, waiting_time=10000):
                self.not_found("data_ano")
            self.click()
            if not self.find( "data_ano_anterior", matching=0.97, waiting_time=10000):
                self.not_found("data_ano_anterior")
            self.click()
            if not self.find( "gerarGrafico", matching=0.97, waiting_time=10000):
                self.not_found("gerarGrafico")
            self.click()
            self.wait(10000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---ITENS COMPRADOS NO PERIODO---####
                             
            if not self.find( "graficos2", matching=0.97, waiting_time=10000):
                self.not_found("graficos2")
            self.click()
            if not self.find( "itensCompradosNoPeriodo", matching=0.97, waiting_time=10000):
                self.not_found("itensCompradosNoPeriodo")
            self.click()
            if not self.find( "data", matching=0.97, waiting_time=10000):
                self.not_found("data")
            self.click_relative(33, 7)
            if not self.find( "data_ano", matching=0.97, waiting_time=10000):
                self.not_found("data_ano")
            self.click()
            if not self.find( "data_ano_anterior", matching=0.97, waiting_time=10000):
                self.not_found("data_ano_anterior")
            self.click()
            if not self.find( "gerarGrafico", matching=0.97, waiting_time=10000):
                self.not_found("gerarGrafico")
            self.click()
            self.wait(10000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---TOTAL COMPRAS FORNECEDORES---####
                             
            if not self.find( "graficos2", matching=0.97, waiting_time=10000):
                self.not_found("graficos2")
            self.click()
            if not self.find( "totalComprasFornecedores", matching=0.97, waiting_time=10000):
                self.not_found("totalComprasFornecedores")
            self.click()
            if not self.find( "data", matching=0.97, waiting_time=10000):
                self.not_found("data")
            self.click_relative(33, 7)
            if not self.find( "data_ano", matching=0.97, waiting_time=10000):
                self.not_found("data_ano")
            self.click()
            if not self.find( "data_ano_anterior", matching=0.97, waiting_time=10000):
                self.not_found("data_ano_anterior")
            self.click()
            if not self.find( "gerarGrafico", matching=0.97, waiting_time=10000):
                self.not_found("gerarGrafico")
            self.click()
            self.wait(10000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---FINANCEIRO POR PLANO FINANCEIRO---####
                             
            if not self.find( "graficos2", matching=0.97, waiting_time=10000):
                self.not_found("graficos2")
            self.click()
            if not self.find( "financeiroPorPlanoFinanceiro", matching=0.97, waiting_time=10000):
                self.not_found("financeiroPorPlanoFinanceiro")
            self.click()
            if not self.find( "b_grupoEmpresa_FinanceiroPorPlano", matching=0.97, waiting_time=10000):
                self.not_found("b_grupoEmpresa_FinanceiroPorPlano")
            self.click_relative(62, 131)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            if not self.find( "data", matching=0.97, waiting_time=10000):
                self.not_found("data")
            self.click_relative(33, 7)
            if not self.find( "data_ano", matching=0.97, waiting_time=10000):
                self.not_found("data_ano")
            self.click()
            if not self.find( "data_ano_anterior", matching=0.97, waiting_time=10000):
                self.not_found("data_ano_anterior")
            self.click()
            if not self.find( "gerarGrafico", matching=0.97, waiting_time=10000):
                self.not_found("gerarGrafico")
            self.click()
            self.wait(10000)
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "fechargestaoadm", matching=0.97, waiting_time=10000):
                self.not_found("fechargestaoadm")
            self.click()
            if not self.find( "simfecharfim", matching=0.97, waiting_time=10000):
                self.not_found("simfecharfim")
            self.click()
            #self.enter()        

            
            def not_found(self, label):
                print(f"Element not found: {label}")  
        
if __name__ == '__main__':
    Bot.main()















































































































































































































































