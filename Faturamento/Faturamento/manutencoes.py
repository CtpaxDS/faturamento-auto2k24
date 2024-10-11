from botcity.core import DesktopBot

class Bot(DesktopBot):
        def action(self, execution=None):
            
            #######################-----LOGIN-----############################
        
            #self.execute(r"C:\Users\Rafael\Desktop\2207\bug\faturamento.exe")
            self.execute(r"C:\Users\Rafael\Desktop\2207\teste23\23mes07\faturamento.exe")
            
            if not self.find( "btn_codigo_usuario", matching=0.97, waiting_time=1000000):
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
            if not self.find( "manutencoes2.0", matching=0.97, waiting_time=100000):
                self.not_found("manutencoes2.0")
            self.click()
            self.wait(1500)
            self.type_down()
            #if not self.find( "manut_clientesfornecedores2.0", matching=0.97, waiting_time=10000):
            #    self.not_found("manut_clientesfornecedores2.0")
            #self.click()
            self.wait(1500)
            self.enter()         
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.wait(3000)
            self.enter()
            if not self.find( "incluirregistro_manut", matching=0.97, waiting_time=10000):
                self.not_found("incluirregistro_manut")
            self.click()
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "alterar_manut", matching=0.97, waiting_time=10000):
                self.not_found("alterar_manut")
            self.click()
            if not self.find( "b_contabilfixo_manut", matching=0.97, waiting_time=10000):
                self.not_found("b_contabilfixo_manut")
            self.click_relative(82, 26)
            self.tab()
            self.tab()
            self.tab()
            self.type_down()
            self.type_down()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_contabilfornecedor_manut", matching=0.97, waiting_time=10000):
                self.not_found("b_contabilfornecedor_manut")
            self.click_relative(78, 25)
            self.tab()
            self.tab()
            self.tab()
            self.type_down()
            self.type_down()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_transportador_manut", matching=0.97, waiting_time=10000):
                self.not_found("b_transportador_manut")
            self.click_relative(79, 24)
            self.type_keys_with_interval(1,'0081260')
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_condpag_manut", matching=0.97, waiting_time=10000):
                self.not_found("b_condpag_manut")
            self.click_relative(79, 25)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "aba2_manutclientes", matching=0.97, waiting_time=10000):
                self.not_found("aba2_manutclientes")
            self.click()
            if not self.find( "b_vendedorcomprador_manutclientes", matching=0.97, waiting_time=10000):
                self.not_found("b_vendedorcomprador_manutclientes")
            self.click_relative(61, 39)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_localcobranca_manutcliente", matching=0.97, waiting_time=10000):
                self.not_found("b_localcobranca_manutcliente")
            self.click_relative(62, 84)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_classificacao_manutcliente", matching=0.97, waiting_time=10000):
                self.not_found("b_classificacao_manutcliente")
            self.click_relative(62, 126)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_regiao_manutcliente", matching=0.97, waiting_time=10000):
                self.not_found("b_regiao_manutcliente")
            self.click_relative(289, 42)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_ramoatividade_manutcliente", matching=0.97, waiting_time=10000):
                self.not_found("b_ramoatividade_manutcliente")
            self.click_relative(288, 82)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_operacao_manutcliente", matching=0.97, waiting_time=10000):
                self.not_found("b_operacao_manutcliente")
            self.click_relative(285, 126)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_estado_manutcliente", matching=0.97, waiting_time=10000):
                self.not_found("b_estado_manutcliente")
            self.click_relative(513, 41)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_segmento_manutcliente", matching=0.97, waiting_time=10000):
                self.not_found("b_segmento_manutcliente")
            self.click_relative(512, 84)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_municipio_manutcliente", matching=0.97, waiting_time=10000):
                self.not_found("b_municipio_manutcliente")
            self.click_relative(739, 39)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_linha_manutcliente", matching=0.97, waiting_time=10000):
                self.not_found("b_linha_manutcliente")
            self.click_relative(741, 80)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            if not self.find( "b_vendaux_manutcliente", matching=0.97, waiting_time=10000):
                self.not_found("b_vendaux_manutcliente")
            self.click_relative(965, 41)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_comissao_manutcliente", matching=0.97, waiting_time=10000):
                self.not_found("b_comissao_manutcliente")
            self.click_relative(967, 83)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_tabpreco_manutcliente", matching=0.97, waiting_time=10000):
                self.not_found("b_tabpreco_manutcliente")
            self.click_relative(947, 128)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_rota_manutcliente", matching=0.97, waiting_time=10000):
                self.not_found("b_rota_manutcliente")
            self.click_relative(1236, 42)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.wait(3000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---CONTRATOS CLIENTES/FORNECEDORES---####
                             
            if not self.find( "manutencoes2.0", matching=0.97, waiting_time=10000):
                self.not_found("manutencoes2.0")
            self.click()
            if not self.find( "contratosdeclientesfornecedores", matching=0.97, waiting_time=10000):
                self.not_found("contratosdeclientesfornecedores")
            self.click()
            if not self.find( "incluirregistro_manut", matching=0.97, waiting_time=10000):
                self.not_found("incluirregistro_manut")
            self.click()
            #self.type_keys_with_interval(1,'0081260')
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "alterar_manut", matching=0.97, waiting_time=10000):
                self.not_found("alterar_manut")
            self.click()
            if not self.find( "b_tipocontrato_manutCC", matching=0.97, waiting_time=10000):
                self.not_found("b_tipocontrato_manutCC")
            self.click_relative(61, 41)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            if not self.find( "b_comissao_manutCC", matching=0.97, waiting_time=10000):
                self.not_found("b_comissao_manutCC")
            self.click_relative(464, 43)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "retornar_alteradados_manutcc", matching=0.97, waiting_time=10000):
                self.not_found("retornar_alteradados_manutcc")
            self.click_relative(40, 42)            
            if not self.find( "aba2_manutclientes", matching=0.97, waiting_time=10000):
                self.not_found("aba2_manutclientes")
            self.click()
            if not self.find( "b_mcc_vendedorcomprador", matching=0.97, waiting_time=10000):
                self.not_found("b_mcc_vendedorcomprador")
            self.click_relative(66, 42)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_mcc_rota", matching=0.97, waiting_time=10000):
                self.not_found("b_mcc_rota")
            self.click_relative(64, 83)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_mcc_linha", matching=0.97, waiting_time=10000):
                self.not_found("b_mcc_linha")
            self.click_relative(64, 125)
            if not self.find( "retornar_consultalinhas", matching=0.97, waiting_time=10000):
                self.not_found("retornar_consultalinhas")
            self.click_relative(33, 47)
            if not self.find( "b_mcc_regiao", matching=0.97, waiting_time=10000):
                self.not_found("b_mcc_regiao")
            self.click_relative(394, 43)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_mcc_localdecobranca", matching=0.97, waiting_time=10000):
                self.not_found("b_mcc_localdecobranca")
            self.click_relative(396, 84)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_mcc_comissao", matching=0.97, waiting_time=10000):
                self.not_found("b_mcc_comissao")
            self.click_relative(394, 126)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_mcc_estado", matching=0.97, waiting_time=10000):
                self.not_found("b_mcc_estado")
            self.click_relative(726, 41)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_mcc_ramoatividade", matching=0.97, waiting_time=10000):
                self.not_found("b_mcc_ramoatividade")
            self.click_relative(725, 85)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_mcc_classificacao", matching=0.97, waiting_time=10000):
                self.not_found("b_mcc_classificacao")
            self.click_relative(721, 121)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_mcc_municipio", matching=0.97, waiting_time=10000):
                self.not_found("b_mcc_municipio")
            self.click_relative(1056, 42)
            self.tab()
            self.tab()
            self.tab()
            self.type_down()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_mcc_segmento", matching=0.97, waiting_time=10000):
                self.not_found("b_mcc_segmento")
            self.click_relative(1055, 81)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_mcc_tipocontrato", matching=0.97, waiting_time=10000):
                self.not_found("b_mcc_tipocontrato")
            self.click_relative(1057, 126)
            self.tab()
            self.tab()
            self.space()
            self.space()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            x=0
            while x<3:
                self.type_down()
                x=x+1
            x=0
            while x<3:
                self.type_up()
                x=x+1
            self.tab()
            x=0
            while x<13:
                self.type_down()
                x=x+1
            x=0
            while x<13:
                self.type_up()
                x=x+1
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            x=0
            while x<6:
                self.backspace()
                x=x+1
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            x=0
            while x<6:
                self.backspace()
                x=x+1
            self.tab()
            self.tab()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            x=0
            while x<6:
                self.backspace()
                x=x+1
            self.tab()
            self.space()
            self.space()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---MANUTENCAO ITENS---####
                             
            if not self.find( "manutencoes2.0", matching=0.97, waiting_time=10000):
                self.not_found("manutencoes2.0")
            self.click()
            if not self.find( "manutencao_itens", matching=0.97, waiting_time=10000):
                self.not_found("manutencao_itens")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.wait(3000)
            if not self.find( "alterar_manut", matching=0.97, waiting_time=10000):
                self.not_found("alterar_manut")
            self.click()
            if not self.find( "b_ncm_MI", matching=0.97, waiting_time=10000):
                self.not_found("b_ncm_MI")
            self.click_relative(170, 64)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_familia_MI", matching=0.97, waiting_time=10000):
                self.not_found("b_familia_MI")
            self.click_relative(52, 46)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_marca_MI", matching=0.97, waiting_time=10000):
                self.not_found("b_marca_MI")
            self.click_relative(54, 91)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_controle_MI", matching=0.97, waiting_time=10000):
                self.not_found("b_controle_MI")
            self.click_relative(53, 127)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_unidadeestoque_MI", matching=0.97, waiting_time=10000):
                self.not_found("b_unidadeestoque_MI")
            self.click_relative(55, 171)
            self.tab()
            self.tab()
            self.tab()
            self.type_down()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_99997_MI", matching=0.97, waiting_time=10000):
                self.not_found("b_99997_MI")
            self.click_relative(53, 213)
            self.tab()
            self.tab()
            self.tab()
            self.type_down()
            self.type_down()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_grupo_MI", matching=0.97, waiting_time=10000):
                self.not_found("b_grupo_MI")
            self.click_relative(385, 43)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_tipo_MI", matching=0.97, waiting_time=10000):
                self.not_found("b_tipo_MI")
            self.click_relative(385, 90)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_centrocusto_MI", matching=0.97, waiting_time=10000):
                self.not_found("b_centrocusto_MI")
            self.click_relative(419, 128)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_grupofiscal_MI", matching=0.97, waiting_time=10000):
                self.not_found("b_grupofiscal_MI")
            self.click_relative(388, 171)
            self.tab()
            self.tab()
            self.tab()
            self.type_down()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_99980_MI", matching=0.97, waiting_time=10000):
                self.not_found("b_99980_MI")
            self.click_relative(386, 213)
            self.tab()
            self.tab()
            self.tab()
            self.type_down()
            self.type_down()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_subgrupos_MI", matching=0.97, waiting_time=10000):
                self.not_found("b_subgrupos_MI")
            self.click_relative(717, 47)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_subtipos_MI", matching=0.97, waiting_time=10000):
                self.not_found("b_subtipos_MI")
            self.click_relative(716, 89)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_cadeiapreco_MI", matching=0.97, waiting_time=10000):
                self.not_found("b_cadeiapreco_MI")
            self.click_relative(720, 130)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_genA_MI", matching=0.97, waiting_time=10000):
                self.not_found("b_genA_MI")
            self.click_relative(717, 173)
            if not self.find( "retornar_generico", matching=0.97, waiting_time=10000):
                self.not_found("retornar_generico")
            self.click_relative(36, 34)
            if not self.find( "b_genB_MI", matching=0.97, waiting_time=10000):
                self.not_found("b_genB_MI")
            self.click_relative(720, 215)
            if not self.find( "retornar_generico", matching=0.97, waiting_time=10000):
                self.not_found("retornar_generico")
            self.click_relative(36, 34)
            if not self.find( "b_fornecedoritem_MI", matching=0.97, waiting_time=10000):
                self.not_found("b_fornecedoritem_MI")
            self.click_relative(62, 24)
            self.wait(500)
            self.type_keys_with_interval(1,'0081260')
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            x=0
            while x<13:
                self.tab()
                x=x+1
            x=0
            while x<10:
                self.type_down()
                x=x+1
            x=0
            while x<10:
                self.type_up()
                x=x+1
            self.tab()
            self.tab()
            self.tab()
            x=0
            while x<8:
                self.type_down()
                x=x+1
            x=0
            while x<8:
                self.type_up()
                x=x+1
            x=0
            while x<4:
                self.tab()
                x=x+1
            x=0
            while x<13:
                self.type_down()
                x=x+1
            x=0
            while x<13:
                self.type_up()
                x=x+1
            self.tab()
            x=0
            while x<4:
                self.type_down()
                x=x+1
            self.tab()
            self.tab()
            x=0
            while x<3:
                self.type_down()
                x=x+1
            x=0
            while x<3:
                self.type_up()
                x=x+1
            self.tab()
            x=0
            while x<3:
                self.type_down()
                x=x+1
            x=0
            while x<3:
                self.type_up()
                x=x+1
            if not self.find( "retornar_alteradados_manutcc", matching=0.97, waiting_time=10000):
                self.not_found("retornar_alteradados_manutcc")
            self.click_relative(40, 42)                  
            if not self.find( "aba2_manutclientes", matching=0.97, waiting_time=10000):
                self.not_found("aba2_manutclientes")
            self.click()
            if not self.find( "b_itemcomp_manutI", matching=0.97, waiting_time=10000):
                self.not_found("b_itemcomp_manutI")
            self.click_relative(55, 108)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "d_periodo1_manutI", matching=0.97, waiting_time=10000):
                self.not_found("d_periodo1_manutI")
            self.click_relative(695, 111)
            if not self.find( "CA_periodo", matching=0.97, waiting_time=10000):
                self.not_found("CA_periodo")
            self.click()
            if not self.find( "CA_periodo_atual", matching=0.97, waiting_time=10000):
                self.not_found("CA_periodo_atual")
            self.click()
            if not self.find( "d_periodo2_manutI", matching=0.97, waiting_time=10000):
                self.not_found("d_periodo2_manutI")
            self.click_relative(931, 110)
            if not self.find( "CA_periodo", matching=0.97, waiting_time=10000):
                self.not_found("CA_periodo")
            self.click()
            if not self.find( "CA_periodo_atual", matching=0.97, waiting_time=10000):
                self.not_found("CA_periodo_atual")
            self.click()
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "d_periodo3_manutI", matching=0.97, waiting_time=10000):
                self.not_found("d_periodo3_manutI")
            self.click_relative(1278, 109)
            if not self.find( "CA_periodo", matching=0.97, waiting_time=10000):
                self.not_found("CA_periodo")
            self.click()
            if not self.find( "CA_periodo_atual", matching=0.97, waiting_time=10000):
                self.not_found("CA_periodo_atual")
            self.click()
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "pesaveis_sim", matching=0.97, waiting_time=10000):
                self.not_found("pesaveis_sim")
            self.click_relative(10, 29)
            if not self.find( "pesaveis_nao", matching=0.97, waiting_time=10000):
                self.not_found("pesaveis_nao")
            self.click_relative(95, 30)
            if not self.find( "pesaveis_todos", matching=0.97, waiting_time=10000):
                self.not_found("pesaveis_todos")
            self.click_relative(159, 29)
            if not self.find( "nme_sim", matching=0.97, waiting_time=10000):
                self.not_found("nme_sim")
            self.click_relative(9, 29)
            if not self.find( "nme_nao", matching=0.97, waiting_time=10000):
                self.not_found("nme_nao")
            self.click_relative(87, 28)
            if not self.find( "nme_todos", matching=0.97, waiting_time=10000):
                self.not_found("nme_todos")
            self.click_relative(161, 31)
            if not self.find( "ie_sim", matching=0.97, waiting_time=10000):
                self.not_found("ie_sim")
            self.click_relative(8, 29)
            if not self.find( "ie_nao", matching=0.97, waiting_time=10000):
                self.not_found("ie_nao")
            self.click_relative(83, 29)
            if not self.find( "ie_todos", matching=0.97, waiting_time=10000):
                self.not_found("ie_todos")
            self.click_relative(159, 27)
            if not self.find( "vnfe_sim", matching=0.97, waiting_time=10000):
                self.not_found("vnfe_sim")
            self.click_relative(9, 29)
            if not self.find( "vnfe_nao", matching=0.97, waiting_time=10000):
                self.not_found("vnfe_nao")
            self.click_relative(84, 30)
            if not self.find( "vnfe_todos", matching=0.97, waiting_time=10000):
                self.not_found("vnfe_todos")
            self.click_relative(158, 30)
            if not self.find( "nfrac_sim", matching=0.97, waiting_time=10000):
                self.not_found("nfrac_sim")
            self.click_relative(9, 29)
            if not self.find( "nfrac_nao", matching=0.97, waiting_time=10000):
                self.not_found("nfrac_nao")
            self.click_relative(83, 30)
            if not self.find( "nfrac_todos", matching=0.97, waiting_time=10000):
                self.not_found("nfrac_todos")
            self.click_relative(158, 29)
            self.tab()
            x=0
            while x<3:
                self.type_down()
                x=x+1
            x=0
            while x<3:
                self.type_up()
                x=x+1
            self.tab()
            x=0
            while x<2:
                self.type_down()
                x=x+1
            x=0
            while x<2:
                self.type_up()
                x=x+1
            self.tab()
            x=0
            while x<9:
                self.type_down()
                x=x+1
            x=0
            while x<9:
                self.type_up()
                x=x+1
            x=0
            while x<7:
                self.tab()
                self.space()
                self.space()
                x=x+1
            self.tab()
            x=0
            while x<4:
                self.tab()
                self.space()
                self.space()
                x=x+1
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---ITENS COMPOSICAO---####
                             
            if not self.find( "manutencoes2.0", matching=0.97, waiting_time=10000):
                self.not_found("manutencoes2.0")
            self.click()
            if not self.find( "itenscomposicao", matching=0.97, waiting_time=10000):
                self.not_found("itenscomposicao")
            self.click()
            if not self.find( "b_composto_manutIC", matching=0.97, waiting_time=10000):
                self.not_found("b_composto_manutIC")
            self.click_relative(126, 82)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "b_substituto_manutIC", matching=0.97, waiting_time=10000):
                self.not_found("b_substituto_manutIC")
            self.click_relative(125, 103)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            x=0
            while x<3:
                self.type_down()
                x=x+1
            x=0
            while x<3:
                self.type_up()
                x=x+1
            if not self.find( "ir_manutIC", matching=0.97, waiting_time=10000):
                self.not_found("ir_manutIC")
            self.click_relative(15, 180)
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
            """
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "quantidade_lancitens", matching=0.97, waiting_time=10000):
                self.not_found("quantidade_lancitens")
            self.click_relative(336, 280)
            self.backspace()
            self.enter()
            x=0
            while x<31:
                self.type_down()
                x=x+1
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            """
            self.type_keys_with_interval(1,'1')
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
            self.enter()
            
                            ####---PRECOS E CUSTOS---####
                             
            if not self.find( "manutencoes2.0", matching=0.97, waiting_time=10000):
                self.not_found("manutencoes2.0")
            self.click()
            if not self.find( "precosecustos", matching=0.97, waiting_time=10000):
                self.not_found("precosecustos")
            self.click()
            if not self.find( "aba2_manutclientes", matching=0.97, waiting_time=10000):
                self.not_found("aba2_manutclientes")
            self.click()
            if not self.find( "b_tabelapreco_manutP", matching=0.97, waiting_time=10000):
                self.not_found("b_tabelapreco_manutP")
            self.click_relative(63, 23)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            self.tab()
            self.tab()
            self.tab()
            self.tab()
            self.tab()
            self.tab()
            x=0
            while x<9:
                self.type_down()
                x=x+1
            x=0
            while x<9:
                self.type_up()
                x=x+1
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.wait(3000)
            if not self.find( "alteracoes_manut", matching=0.97, waiting_time=10000):
                self.not_found("alteracoes_manut")
            self.click()
            if not self.find( "a_geralcomformula", matching=0.97, waiting_time=10000):
                self.not_found("a_geralcomformula")
            self.click()
            if not self.find( "retorna_p1_manut", matching=0.97, waiting_time=10000):
                self.not_found("retorna_p1_manut")
            self.click_relative(51, 39)
            if not self.find( "alteracoes_manut", matching=0.97, waiting_time=10000):
                self.not_found("alteracoes_manut")
            self.click()
            """
            if not self.find( "a_individualcomformula", matching=0.97, waiting_time=10000):
                self.not_found("a_individualcomformula")
            self.click()
            if not self.find( "b_operacao_p2manut", matching=0.97, waiting_time=10000):
                self.not_found("b_operacao_p2manut")
            self.click_relative(65, 194)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_regiao_p2manut", matching=0.97, waiting_time=10000):
                self.not_found("b_regiao_p2manut")
            self.click_relative(430, 199)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "retornar_p2manut", matching=0.97, waiting_time=10000):
                self.not_found("retornar_p2manut")
            self.click_relative(24, 39)
            self.type_right()
            self.enter()
            
            if not self.find( "alteracoes_manut", matching=0.97, waiting_time=10000):
                self.not_found("alteracoes_manut")
            self.click()
            """
            if not self.find( "a_p3geral_manut", matching=0.97, waiting_time=10000):
                self.not_found("a_p3geral_manut")
            self.click()
            if not self.find( "retornar_manut_geral", matching=0.97, waiting_time=10000):
                self.not_found("retornar_manut_geral")
            self.click_relative(39, 39)
            if not self.find( "alteracoes_manut", matching=0.97, waiting_time=10000):
                self.not_found("alteracoes_manut")
            self.click()
            if not self.find( "a_individual_p4manut", matching=0.97, waiting_time=10000):
                self.not_found("a_individual_p4manut")
            self.click()
            if not self.find( "b_item_p4manut", matching=0.97, waiting_time=10000):
                self.not_found("b_item_p4manut")
            self.click_relative(160, 110)
            self.wait(500)
            if not self.find( "b_item_p4manut", matching=0.97, waiting_time=10000):
                self.not_found("b_item_p4manut")
            self.click_relative(160, 110)
            self.enter()
            x=0
            while x<31:
                self.type_down()
                x=x+1
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "retornar_p4manut", matching=0.97, waiting_time=10000):
                self.not_found("retornar_p4manut")
            self.click_relative(36, 35)
            if not self.find( "alteracoes_manut", matching=0.97, waiting_time=10000):
                self.not_found("alteracoes_manut")
            self.click()
            if not self.find( "a_p5manut", matching=0.97, waiting_time=10000):
                self.not_found("a_p5manut")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "alteracoes_manut", matching=0.97, waiting_time=10000):
                self.not_found("alteracoes_manut")
            self.click()
            if not self.find( "a_p6manut", matching=0.97, waiting_time=10000):
                self.not_found("a_p6manut")
            self.click()
            self.wait(10000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.enter()
            self.enter()
            self.wait(1000)

                            ####---OFERTAS---####
                             
            if not self.find( "manutencoes2.0", matching=0.97, waiting_time=10000):
                self.not_found("manutencoes2.0")
            self.click()
            self.wait(1000)
            if not self.find( "ofertas", matching=0.97, waiting_time=10000):
                self.not_found("ofertas")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---SERVIÇOS---####
            
            if not self.find( "manutencoes2.0", matching=0.97, waiting_time=10000):
                self.not_found("manutencoes2.0")
            self.click()
            if not self.find( "manutservicos", matching=0.97, waiting_time=10000):
                self.not_found("manutservicos")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "aba2_manutclientes", matching=0.97, waiting_time=10000):
                self.not_found("aba2_manutclientes")
            self.click()
            if not self.find( "b_tabpreco_manutserv", matching=0.97, waiting_time=10000):
                self.not_found("b_tabpreco_manutserv")
            self.click_relative(55, 199)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            """
            if not self.find( "alterar_manut", matching=0.97, waiting_time=10000):
                self.not_found("alterar_manut")
            self.click()
            if not self.find( "b_familia_mserv", matching=0.97, waiting_time=10000):
                self.not_found("b_familia_mserv")
            self.click_relative(52, 170)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            if not self.find( "b_marca_mserv", matching=0.97, waiting_time=10000):
                self.not_found("b_marca_mserv")
            self.click_relative(54, 211)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            if not self.find( "b_uniest_mserv", matching=0.97, waiting_time=10000):
                self.not_found("b_uniest_mserv")
            self.click_relative(54, 251)
            self.tab()
            self.tab()
            self.tab()
            self.type_down()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            if not self.find( "b_grupo_mserv", matching=0.97, waiting_time=10000):
                self.not_found("b_grupo_mserv")
            self.click_relative(386, 170)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            if not self.find( "b_grupofiscal_mserv", matching=0.97, waiting_time=10000):
                self.not_found("b_grupofiscal_mserv")
            self.click_relative(385, 210)
            self.tab()
            self.tab()
            self.tab()
            self.type_down()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_subgrupo_mserv", matching=0.97, waiting_time=10000):
                self.not_found("b_subgrupo_mserv")
            self.click_relative(721, 169)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_planodecontas_mserv", matching=0.97, waiting_time=10000):
                self.not_found("b_planodecontas_mserv")
            self.click_relative(718, 211)
            self.tab()
            self.tab()
            self.tab()
            self.type_down()
            self.type_down()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_alteradados_mserv", matching=0.97, waiting_time=10000):
                self.not_found("b_alteradados_mserv")
            self.click_relative(39, 40)
            """
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---SERVICOS PRECOS---####
                             
            if not self.find( "manutencoes2.0", matching=0.97, waiting_time=10000):
                self.not_found("manutencoes2.0")
            self.click()
            if not self.find( "servicoprecos", matching=0.97, waiting_time=10000):
                self.not_found("servicoprecos")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "alteracoes_manut", matching=0.97, waiting_time=10000):
                self.not_found("alteracoes_manut")
            self.click()
            if not self.find( "alteracoesprecotabela", matching=0.97, waiting_time=10000):
                self.not_found("alteracoesprecotabela")
            self.click()
            self.type_left()
            self.enter()
            if not self.find( "alteracoes_manut", matching=0.97, waiting_time=10000):
                self.not_found("alteracoes_manut")
            self.click()
            if not self.find( "alteracoesprecotabela", matching=0.97, waiting_time=10000):
                self.not_found("alteracoesprecotabela")
            self.click()
            self.type_left()
            self.type_left()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.enter()
            
                            ####---NCM---####
                             
            if not self.find( "manutencoes2.0", matching=0.97, waiting_time=10000):
                self.not_found("manutencoes2.0")
            self.click()
            if not self.find( "NCMmanut", matching=0.97, waiting_time=10000):
                self.not_found("NCMmanut")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "alterar_manut", matching=0.97, waiting_time=10000):
                self.not_found("alterar_manut")
            self.click()
            if not self.find( "retornar_altera_NCM", matching=0.97, waiting_time=10000):
                self.not_found("retornar_altera_NCM")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---ESTADOS NCM---####
                             
            if not self.find( "manutencoes2.0", matching=0.97, waiting_time=10000):
                self.not_found("manutencoes2.0")
            self.click()
            if not self.find( "esstadosNCM_manut", matching=0.97, waiting_time=10000):
                self.not_found("esstadosNCM_manut")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "alterar_manut", matching=0.97, waiting_time=10000):
                self.not_found("alterar_manut")
            self.click()
            self.tab()
            self.tab()
            x=0
            while x<10:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            if not self.find( "retorna_dadosENCM", matching=0.97, waiting_time=10000):
                self.not_found("retorna_dadosENCM")
            self.click_relative(43, 44) 
            if not self.find( "addregistro_manutecnm", matching=0.97, waiting_time=10000):
                self.not_found("addregistro_manutecnm")
            self.click()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---MANUT CONDICAO PAGAMENTO---####
            
            if not self.find( "manutencoes2.0", matching=0.97, waiting_time=10000):
                self.not_found("manutencoes2.0")
            self.click()
            if not self.find( "manutcondpagamento", matching=0.97, waiting_time=10000):
                self.not_found("manutcondpagamento")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "alterar_manut", matching=0.97, waiting_time=10000):
                self.not_found("alterar_manut")
            self.click()
            
                            ####---RECALCULO CUSTO MEDIO MERCANTIL---####
                             
            if not self.find( "manutencoes2.0", matching=0.97, waiting_time=10000):
                self.not_found("manutencoes2.0")
            self.click()
            if not self.find( "recalculocustomediomercantilmanut", matching=0.97, waiting_time=10000):
                self.not_found("recalculocustomediomercantilmanut")
            self.click()
            if not self.find( "aba2_recalculocustomedio_manut", matching=0.97, waiting_time=10000):
                self.not_found("aba2_recalculocustomedio_manut")
            self.click()
            
            if not self.find( "b_item_manutRCmedio", matching=0.97, waiting_time=10000):
                self.not_found("b_item_manutRCmedio")
            self.click_relative(72, 169)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.wait(2000)
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            if not self.find( "b_operacao_RCmedio", matching=0.97, waiting_time=10000):
                self.not_found("b_operacao_RCmedio")
            self.click_relative(65, 191)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.tab()
            self.type_up()
            x=0
            while x<3:
                self.type_down()
                x=x+1
            x=0
            while x<3:
                self.type_up()
                x=x+1
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.tab()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "addregistro_manutecnm", matching=0.97, waiting_time=10000):
                self.not_found("addregistro_manutecnm")
            self.click()
            if not self.find( "b_lancitens_manut", matching=0.97, waiting_time=10000):
                self.not_found("b_lancitens_manut")
            self.click_relative(14, 34)
            self.type_keys_with_interval(1,'agulha gengival')
            self.enter()
            self.type_down()
            self.type_down()
            self.type_down()
            self.type_down()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(2000)
            self.type_keys_with_interval(1,'1')
            self.tab()
            self.tab()
            self.tab()
            self.tab()
            self.tab()
            self.enter()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.backspace()
            self.tab()
            if not self.find( "p_reccustomedio", matching=0.97, waiting_time=10000):
                self.not_found("p_reccustomedio")
            self.click_relative(230, 88)            
            if not self.find( "CA_periodo", matching=0.97, waiting_time=10000):
                self.not_found("CA_periodo")
            self.click()
            if not self.find( "CA_periodo_atual", matching=0.97, waiting_time=10000):
                self.not_found("CA_periodo_atual")
            self.click()
            """
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.enter()
            if not self.find( "s_codteste_recmedio", matching=0.97, waiting_time=10000):
                self.not_found("s_codteste_recmedio")
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
            """
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---MANUT MOV FRETES---####
                             
            if not self.find( "manutencoes2.0", matching=0.97, waiting_time=10000):
                self.not_found("manutencoes2.0")
            self.click()
            if not self.find( "manutmovfretes_aba", matching=0.97, waiting_time=10000):
                self.not_found("manutmovfretes_aba")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()                 
            if not self.find( "alterar_manut", matching=0.97, waiting_time=10000):
                self.not_found("alterar_manut")
            self.click()
            if not self.find( "b_operacao_alteradados_manutfrete", matching=0.97, waiting_time=10000):
                self.not_found("b_operacao_alteradados_manutfrete")
            self.click_relative(71, 111)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_cfop_alteradados_manutfrete", matching=0.97, waiting_time=10000):
                self.not_found("b_cfop_alteradados_manutfrete")
            self.click_relative(465, 111)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "retornar_alteradados_manutfrete", matching=0.97, waiting_time=10000):
                self.not_found("retornar_alteradados_manutfrete")
            self.click_relative(44, 41)
            if not self.find( "b_transportador_manutfrete", matching=0.97, waiting_time=10000):
                self.not_found("b_transportador_manutfrete")
            self.click_relative(421, 85)
            self.type_keys_with_interval(1,'0081260')
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---ESTOQUE---####
                             
            if not self.find( "estoque4.1", matching=0.97, waiting_time=10000):
                self.not_found("estoque4.1")
            self.click()   
            self.type_down()                     
            self.enter()                      
            self.wait(1500)
            self.enter()
            if not self.find( "aba2_estoque_entradasaidaserv", matching=0.97, waiting_time=10000):
                self.not_found("aba2_estoque_entradasaidaserv")
            self.click()
            if not self.find( "b_codop_meserv", matching=0.97, waiting_time=10000):
                self.not_found("b_codop_meserv")
            self.click_relative(74, 321)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "b_condpag_mserv", matching=0.97, waiting_time=10000):
                self.not_found("b_condpag_mserv")
            self.click_relative(71, 359)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "b_cfop_meserv", matching=0.97, waiting_time=10000):
                self.not_found("b_cfop_meserv")
            self.click_relative(74, 403)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "b_item_meserv", matching=0.97, waiting_time=10000):
                self.not_found("b_item_meserv")
            self.click_relative(72, 444)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "b_class_meserv", matching=0.97, waiting_time=10000):
                self.not_found("b_class_meserv")
            self.click_relative(473, 322)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "b_transportador_meserv", matching=0.97, waiting_time=10000):
                self.not_found("b_transportador_meserv")
            self.click_relative(471, 362)
            self.type_keys_with_interval(1,'0081260')
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "b_centrocustoserv_meserv", matching=0.97, waiting_time=10000):
                self.not_found("b_centrocustoserv_meserv")
            self.click_relative(493, 402)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "b_servico_meserv", matching=0.97, waiting_time=10000):
                self.not_found("b_servico_meserv")
            self.click_relative(473, 445)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.enter()
            if not self.find( "b_vendedor_meserv", matching=0.97, waiting_time=10000):
                self.not_found("b_vendedor_meserv")
            self.click_relative(873, 319)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            self.tab()
            self.backspace()
            self.tab()

            if not self.find( "b_rota_meserv", matching=0.97, waiting_time=10000):
                self.not_found("b_rota_meserv")
            self.click_relative(873, 363)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "b_centrocustoitem_meserv", matching=0.97, waiting_time=10000):
                self.not_found("b_centrocustoitem_meserv")
            self.click_relative(893, 403)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.wait(2000)
            self.type_keys_with_interval(1,'8748')
            self.tab()
            self.type_keys_with_interval(1,'99')
            self.tab()
            self.type_keys_with_interval(1,'99')
            self.tab()
            x=0
            while x<40:
                self.type_down()
                x=x+1
            x=0
            while x<39:
                self.type_up()
                x=x+1
            self.tab()
            x=0
            while x<12:
                self.type_down()
                x=x+1
            x=0
            while x<12:
                self.type_up()
                x=x+1
            self.tab()
            if not self.find( "b_codoperacao_MI_estoque", matching=0.97, waiting_time=10000):
                self.not_found("b_codoperacao_MI_estoque")
            self.click_relative(68, 158)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_cfop_MI_estoque", matching=0.97, waiting_time=10000):
                self.not_found("b_cfop_MI_estoque")
            self.click_relative(68, 199)
            self.backspace()
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_condpag_MI_estoque", matching=0.97, waiting_time=10000):
                self.not_found("b_condpag_MI_estoque")
            self.click_relative(433, 197)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_fornecedor_MI_estoque", matching=0.97, waiting_time=10000):
                self.not_found("b_fornecedor_MI_estoque")
            self.click_relative(210, 298)
            self.wait(2000)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_comprador_MI_estoque", matching=0.97, waiting_time=10000):
                self.not_found("b_comprador_MI_estoque")
            self.click_relative(439, 439)
            self.wait(2000)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_rota_MI_estoque", matching=0.97, waiting_time=10000):
                self.not_found("b_rota_MI_estoque")
            self.click_relative(68, 479)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.tab()
            self.tab()
            x=0
            while x<8:
                self.type_down()
                x=x+1
            x=0
            while x<8:
                self.type_up()
                x=x+1
            self.tab()
            x=0
            while x<5:
                self.type_down()
                x=x+1
            x=0
            while x<5:
                self.type_up()
                x=x+1
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            if not self.find( "b_centrocusto_MI_estoque", matching=0.97, waiting_time=10000):
                self.not_found("b_centrocusto_MI_estoque")
            self.click_relative(82, 26)
            self.backspace()
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.backspace()
            self.tab()
            if not self.find( "b_transportador_MI_estoque", matching=0.97, waiting_time=10000):
                self.not_found("b_transportador_MI_estoque")
            self.click_relative(66, 25)
            self.enter()
            self.wait(1000)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.tab()
            self.type_up()
            x=0
            while x<5:
                self.type_down()
                x=x+1
            x=0
            while x<4:
                self.type_up()
                x=x+1
            self.tab()
            if not self.find( "b_municipiocoleta_MI_estoque", matching=0.97, waiting_time=10000):
                self.not_found("b_municipiocoleta_MI_estoque")
            self.click_relative(56, 25)
            self.tab()
            self.tab()
            self.tab()
            self.type_down()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_municipioentrega_MI_estoque", matching=0.97, waiting_time=10000):
                self.not_found("b_municipioentrega_MI_estoque")
            self.click_relative(59, 24)
            self.tab()
            self.tab()
            self.tab()
            self.type_down()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.tab()
            if not self.find( "b_classificacao_MI_estoque", matching=0.97, waiting_time=10000):
                self.not_found("b_classificacao_MI_estoque")
            self.click_relative(57, 25)
            self.backspace()
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "aba2_MI_estoque", matching=0.97, waiting_time=10000):
                self.not_found("aba2_MI_estoque")
            self.click()
            if not self.find( "incluir_movimentoitens_MI_estoque", matching=0.97, waiting_time=10000):
                self.not_found("incluir_movimentoitens_MI_estoque")
            self.click_relative(14, 141)
            self.enter()
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
            self.type_keys_with_interval(1,'1')
            if not self.find( "botaoconfirmaritensreqcompras", matching=0.97, waiting_time=10000):
                self.not_found("botaoconfirmaritensreqcompras")
            self.click()
            self.wait(3000)
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'1')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "b_lotenumero_MI_estoque", matching=0.97, waiting_time=10000):
                self.not_found("b_lotenumero_MI_estoque")
            self.click_relative(207, 194)
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
            self.wait(1500)
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.wait(2000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---ABA3 MI_ESTOQUE---####
            
            if not self.find( "aba3_MI_estoque", matching=0.97, waiting_time=10000):
                self.not_found("aba3_MI_estoque")
            self.click()
            if not self.find( "b_servico_MI_estoque_a3", matching=0.97, waiting_time=10000):
                self.not_found("b_servico_MI_estoque_a3")
            self.click_relative(70, 152)
            self.type_down()
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            self.tab()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'1')
            if not self.find( "b_classificacao_MI_estoque_a3", matching=0.97, waiting_time=10000):
                self.not_found("b_classificacao_MI_estoque_a3")
            self.click_relative(72, 241)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            #if not self.find( "b_centrocusto_MI_estoque_a3", matching=0.97, waiting_time=10000):
            #    self.not_found("b_centrocusto_MI_estoque_a3")
            #self.click_relative(512, 200)
            #if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
            #    self.not_found("retornarpe")
            #self.click()
            if not self.find( "gravar_a3_MI_estoque", matching=0.97, waiting_time=10000):
                self.not_found("gravar_a3_MI_estoque")
            self.click()
            self.enter()
            #if not self.find( "b_cfop_MI_estoque_a3", matching=0.97, waiting_time=10000):
            #    self.not_found("b_cfop_MI_estoque_a3")
            #self.click_relative(75, 203)
            #if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
            #    self.not_found("selecionarmunicipiovcr")
            #self.click()
            self.wait(500)
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'123')
            #x=0
            #while x<6:
            #    if not self.find( "loop_tipotributacao_MI_estoque_a3", matching=0.97, waiting_time=10000):
            #        self.not_found("loop_tipotributacao_MI_estoque_a3")
            #    self.click_relative(396, 260)
            #    self.type_down()
            #    self.enter()
            #    x=x+1
            """
            x=0
            while x<21:
                self.type_down()
                x=x+1
            x=0
            while x<6:
                if not self.find( "loop_tipotributacao2_MI_estoque_a3", matching=0.97, waiting_time=10000):
                    self.not_found("loop_tipotributacao2_MI_estoque_a3")
                self.click_relative(397, 311)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<33:
                self.type_down()
                x=x+1
            self.tab()
            x=0
            while x<4:
                self.type_down()
                x=x+1
            x=0
            while x<6:
                if not self.find( "loop_tipotributacao3_MI_estoque_a3", matching=0.97, waiting_time=10000):
                    self.not_found("loop_tipotributacao3_MI_estoque_a3")
                self.click_relative(397, 348)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<33:
                self.type_down()
                x=x+1
            self.tab()
            x=0
            while x<19:
                self.type_down()
                x=x+1
            if not self.find( "b_centrocusto_MI_estoque_a3", matching=0.97, waiting_time=10000):
                self.not_found("b_centrocusto_MI_estoque_a3")
            self.click_relative(96, 453)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            """
            self.enter()
            #if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
            #    self.not_found("retornarpe")
            #self.click()
            #if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
            #    self.not_found("salvarrs")
            #self.click()
            self.wait(1000)
            self.key_esc()
            #self.enter()
            self.wait(1000)
            if not self.find( "aba4_MI_estoque", matching=0.97, waiting_time=10000):
                self.not_found("aba4_MI_estoque")
            self.click()
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "aba3_todos_estoque", matching=0.97, waiting_time=10000):
                self.not_found("aba3_todos_estoque")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            #if not self.find( "desliberar_movItens_testesubs", matching=0.97, waiting_time=10000):
            #    self.not_found("desliberar_movItens_testesubs")
            #self.click()
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
            
                            ####---ENTRADA E SAIDA RAPIDA---####
            
            if not self.find( "estoque4.1", matching=0.97, waiting_time=10000):
                self.not_found("estoque4.1")
            self.click()
            if not self.find( "entradasaidarapida_estoque", matching=0.97, waiting_time=10000):
                self.not_found("entradasaidarapida_estoque")
            self.click()
            self.wait(2000)
            self.enter()
            if not self.find( "aba2_estoque_entradasaidaserv", matching=0.97, waiting_time=10000):
                self.not_found("aba2_estoque_entradasaidaserv")
            self.click()
            if not self.find( "a_cliente_MESIS_estoque", matching=0.97, waiting_time=10000):
                self.not_found("a_cliente_MESIS_estoque")
            self.click_relative(517, 91)
            if not self.find( "b_cliente_MESIS_estoque", matching=0.97, waiting_time=10000):
                self.not_found("b_cliente_MESIS_estoque")
            self.click_relative(511, 115)
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
            """
            if not self.find( "b_codop_MESIS_estoque", matching=0.97, waiting_time=10000):
                self.not_found("b_codop_MESIS_estoque")
            self.click_relative(63, 41)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "b_condpag_MESIS_estoque", matching=0.97, waiting_time=10000):
                self.not_found("b_condpag_MESIS_estoque")
            self.click_relative(64, 81)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "b_cfop_MESIS_estoque", matching=0.97, waiting_time=10000):
                self.not_found("b_cfop_MESIS_estoque")
            self.click_relative(64, 126)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "b_item_MESIS_estoque", matching=0.97, waiting_time=10000):
                self.not_found("b_item_MESIS_estoque")
            self.click_relative(65, 167)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            """
            if not self.find( "b_codop_meserv", matching=0.97, waiting_time=10000):
                self.not_found("b_codop_meserv")
            self.click_relative(74, 321)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "b_condpag_mserv", matching=0.97, waiting_time=10000):
                self.not_found("b_condpag_mserv")
            self.click_relative(71, 359)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "b_cfop_meserv", matching=0.97, waiting_time=10000):
                self.not_found("b_cfop_meserv")
            self.click_relative(74, 403)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "b_item_meserv", matching=0.97, waiting_time=10000):
                self.not_found("b_item_meserv")
            self.click_relative(72, 444)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "b_class_meserv", matching=0.97, waiting_time=10000):
                self.not_found("b_class_meserv")
            self.click_relative(473, 322)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "b_transportador_meserv", matching=0.97, waiting_time=10000):
                self.not_found("b_transportador_meserv")
            self.click_relative(471, 362)
            self.type_keys_with_interval(1,'0081260')
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "b_centrocustoserv_meserv", matching=0.97, waiting_time=10000):
                self.not_found("b_centrocustoserv_meserv")
            self.click_relative(493, 402)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "b_servico_meserv", matching=0.97, waiting_time=10000):
                self.not_found("b_servico_meserv")
            self.click_relative(473, 445)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "b_vendedor_meserv", matching=0.97, waiting_time=10000):
                self.not_found("b_vendedor_meserv")
            self.click_relative(873, 319)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.enter()
            self.wait(500)
            self.backspace()
            self.backspace()
            self.tab()
            self.tab()
            if not self.find( "b_rota_meserv", matching=0.97, waiting_time=10000):
                self.not_found("b_rota_meserv")
            self.click_relative(873, 363)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "b_centrocustoitem_meserv", matching=0.97, waiting_time=10000):
                self.not_found("b_centrocustoitem_meserv")
            self.click_relative(893, 403)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.wait(2000)
            if not self.find( "b_codigoOperacao_MRI", matching=0.97, waiting_time=10000):
                self.not_found("b_codigoOperacao_MRI")
            self.click_relative(66, 160)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_cliente_MRI", matching=0.97, waiting_time=10000):
                self.not_found("b_cliente_MRI")
            self.click_relative(68, 198)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.wait(500)
            """
            if not self.find( "b_centroCusto_MRI", matching=0.97, waiting_time=10000):
                self.not_found("b_centroCusto_MRI")
            self.click_relative(90, 242)
            self.backspace()
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.backspace()"""            
            #if not self.find( "b_operacao_MRI_estoque", matching=0.97, waiting_time=10000):
            #    self.not_found("b_operacao_MRI_estoque")
            #self.click_relative(483, 107)
            #self.enter()
            #if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
            #    self.not_found("selecionarmunicipiovcr")
            #self.click()
            #self.wait(500)
            #x=0
            #while x<6:
            #    self.tab()
            #    x=x+1
            #self.type_keys_with_interval(1,'te12!@')
            if not self.find( "ir_MRI_estoquerapido", matching=0.97, waiting_time=10000):
                self.not_found("ir_MRI_estoquerapido")
            self.click_relative(11, 325)
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
            self.type_keys_with_interval(1,'1')
            if not self.find( "botaoconfirmaritensreqcompras", matching=0.97, waiting_time=10000):
                self.not_found("botaoconfirmaritensreqcompras")
            self.click()
            self.wait(3000)
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'1')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "b_lotenumero_MI_estoque", matching=0.97, waiting_time=10000):
                self.not_found("b_lotenumero_MI_estoque")
            self.click_relative(207, 194)
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
            self.wait(2000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "a2_selecao_testeG", matching=0.97, waiting_time=10000):
                self.not_found("a2_selecao_testeG")
            self.click_relative(57, 147)
            if not self.find( "apagar_vendedor_testeG", matching=0.97, waiting_time=10000):
                self.not_found("apagar_vendedor_testeG")
            self.double_click_relative(835, 41)
            self.backspace()
            if not self.find( "aba3_todos_estoque", matching=0.97, waiting_time=10000):
                self.not_found("aba3_todos_estoque")
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
            
                            ####---ALMOXARIFADO---####
                             
            if not self.find( "estoque4.1", matching=0.97, waiting_time=10000):
                self.not_found("estoque4.1")
            self.click()
            if not self.find( "almoxarifado", matching=0.97, waiting_time=10000):
                self.not_found("almoxarifado")
            self.click()
            if not self.find( "almoxarifado", matching=0.97, waiting_time=10000):
                self.not_found("almoxarifado")
            self.click()
            self.wait(3000)
            self.enter()
            if not self.find( "aba2_estoque_entradasaidaserv", matching=0.97, waiting_time=10000):
                self.not_found("aba2_estoque_entradasaidaserv")
            self.click()
            if not self.find( "b_codop_MESIS_estoque", matching=0.97, waiting_time=10000):
                self.not_found("b_codop_MESIS_estoque")
            self.click_relative(63, 41)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "b_condpag_MESIS_estoque", matching=0.97, waiting_time=10000):
                self.not_found("b_condpag_MESIS_estoque")
            self.click_relative(64, 81)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "b_cfop_MESIS_estoque", matching=0.97, waiting_time=10000):
                self.not_found("b_cfop_MESIS_estoque")
            self.click_relative(64, 126)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "b_item_MESIS_estoque", matching=0.97, waiting_time=10000):
                self.not_found("b_item_MESIS_estoque")
            self.click_relative(65, 167)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "b_classificacao_CMIA_almoxarifado", matching=0.97, waiting_time=10000):
                self.not_found("b_classificacao_CMIA_almoxarifado")
            self.click_relative(464, 44)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "b_transportador_CMIA_almoxarifado", matching=0.97, waiting_time=10000):
                self.not_found("b_transportador_CMIA_almoxarifado")
            self.click_relative(465, 82)
            self.enter()
            self.type_down()
            self.type_down()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "b_centrocusto_servico_CMIA_almoxarifado", matching=0.97, waiting_time=10000):
                self.not_found("b_centrocusto_servico_CMIA_almoxarifado")
            self.click_relative(485, 126)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "b_servico_CMIA_almoxarifado", matching=0.97, waiting_time=10000):
                self.not_found("b_servico_CMIA_almoxarifado")
            self.click_relative(467, 167)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.enter()
            if not self.find( "b_vendedor_CMIA_almoxarifado", matching=0.97, waiting_time=10000):
                self.not_found("b_vendedor_CMIA_almoxarifado")
            self.click_relative(865, 41)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "b_rota_CMIA_almoxarifado", matching=0.97, waiting_time=10000):
                self.not_found("b_rota_CMIA_almoxarifado")
            self.click_relative(861, 85)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "b_centrocusto_itens_CMIA_almoxarifado", matching=0.97, waiting_time=10000):
                self.not_found("b_centrocusto_itens_CMIA_almoxarifado")
            self.click_relative(886, 123)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.wait(2000)
            self.tab()
            self.type_keys_with_interval(1,'123')            
            if not self.find( "b_operacao_MA_almoxarifado", matching=0.97, waiting_time=10000):
                self.not_found("b_operacao_MA_almoxarifado")
            self.click_relative(63, 160)
            if not self.find( "aba2_selecao_teste1", matching=0.97, waiting_time=10000):
                self.not_found("aba2_selecao_teste1")
            self.click()
            if not self.find( "todos_selecao_teste1", matching=0.97, waiting_time=10000):
                self.not_found("todos_selecao_teste1")
            self.click_relative(-4, 248)
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'22')
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_centrodecusto_MA_almoxarifado", matching=0.97, waiting_time=10000):
                self.not_found("b_centrodecusto_MA_almoxarifado")
            self.click_relative(96, 204)
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
            if not self.find( "ir_MA_almoxarifado", matching=0.97, waiting_time=10000):
                self.not_found("ir_MA_almoxarifado")
            self.click_relative(14, 334)
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
            self.type_keys_with_interval(1,'1')
            if not self.find( "botaoconfirmaritensreqcompras", matching=0.97, waiting_time=10000):
                self.not_found("botaoconfirmaritensreqcompras")
            self.click()
            self.wait(3000)
            #if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
            #    self.not_found("incluirpe")
            #self.click()
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'1')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "b_lotenumero_MI_almoxarifado_2.0", matching=0.97, waiting_time=10000):
                self.not_found("b_lotenumero_MI_almoxarifado_2.0")
            self.click_relative(207, 192)
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
            self.wait(2000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "aba3_todos_estoque", matching=0.97, waiting_time=10000):
                self.not_found("aba3_todos_estoque")
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
            
                            ####---ALMOXARIFADO OSM SAIDA---####
                             
            if not self.find( "estoque4.1", matching=0.97, waiting_time=10000):
                self.not_found("estoque4.1")
            self.click()
            if not self.find( "almoxarifado", matching=0.97, waiting_time=10000):
                self.not_found("almoxarifado")
            self.click()
            if not self.find( "almoxarifadoOSMsaida", matching=0.97, waiting_time=10000):
                self.not_found("almoxarifadoOSMsaida")
            self.click()
            if not self.find( "b_classificacao_saida_almoxarifado", matching=0.97, waiting_time=10000):
                self.not_found("b_classificacao_saida_almoxarifado")
            self.click_relative(91, 313)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "aba2_consulta_saida_almoxarifado", matching=0.97, waiting_time=10000):
                self.not_found("aba2_consulta_saida_almoxarifado")
            self.click()
            if not self.find( "b_cliente_saida_almoxarifado", matching=0.97, waiting_time=10000):
                self.not_found("b_cliente_saida_almoxarifado")
            self.click_relative(298, 141)
            self.enter()
            x=0
            while x<18:
                self.type_down()
                x=x+1
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_projeto_saida_almoxarifado", matching=0.97, waiting_time=10000):
                self.not_found("b_projeto_saida_almoxarifado")
            self.click_relative(986, 140)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---ALMOXARIFADO OSM DEVOLUCAO---####
                             
            if not self.find( "estoque4.1", matching=0.97, waiting_time=10000):
                self.not_found("estoque4.1")
            self.click()
            if not self.find( "almoxarifado", matching=0.97, waiting_time=10000):
                self.not_found("almoxarifado")
            self.click()
            if not self.find( "almoxarifadoOSMdevolucao", matching=0.97, waiting_time=10000):
                self.not_found("almoxarifadoOSMdevolucao")
            self.click()
            if not self.find( "b_entrada_almoxarifado_padrao", matching=0.97, waiting_time=10000):
                self.not_found("b_entrada_almoxarifado_padrao")            
            self.click_relative(91, 313)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "aba2_consulta_saida_almoxarifado", matching=0.97, waiting_time=10000):
                self.not_found("aba2_consulta_saida_almoxarifado")
            self.click()
            if not self.find( "b_entrada_almoxarifado_padrao", matching=0.97, waiting_time=10000):
                self.not_found("b_entrada_almoxarifado_padrao")
            self.click_relative(298, 141)
            self.enter()
            x=0
            while x<18:
                self.type_down()
                x=x+1
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_entrada_almoxarifado_padrao", matching=0.97, waiting_time=10000):
                self.not_found("b_entrada_almoxarifado_padrao")
            self.click_relative(986, 140)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---SOLICITAÇÃO---####
                             
            if not self.find( "estoque4.1", matching=0.97, waiting_time=10000):
                self.not_found("estoque4.1")
            self.click()
            if not self.find( "almoxarifado", matching=0.97, waiting_time=10000):
                self.not_found("almoxarifado")
            self.click()
            if not self.find( "solicitacao_almoxarifado", matching=0.97, waiting_time=10000):
                self.not_found("solicitacao_almoxarifado")
            self.click()
            if not self.find( "selecao_solicitacao_almoxarifado", matching=0.97, waiting_time=10000):
                self.not_found("selecao_solicitacao_almoxarifado")
            self.click()
            if not self.find( "b_item_solicitacao_almoxarifado", matching=0.97, waiting_time=10000):
                self.not_found("b_item_solicitacao_almoxarifado")
            self.click_relative(73, 165)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_classificacao_solicitacao_almoxarifado", matching=0.97, waiting_time=10000):
                self.not_found("b_classificacao_solicitacao_almoxarifado")
            self.click_relative(67, 212)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_centrocusto_solicitacao_almoxarifado", matching=0.97, waiting_time=10000):
                self.not_found("b_centrocusto_solicitacao_almoxarifado")
            self.click_relative(474, 213)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()  
            if not self.find( "b_solicitante_solicitacao_almoxarifado", matching=0.97, waiting_time=10000):
                self.not_found("b_solicitante_solicitacao_almoxarifado")
            self.click_relative(62, 150)
            self.type_keys_with_interval(1,'cadastro')
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_cliente_solicitacao_almoxarifado", matching=0.97, waiting_time=10000):
                self.not_found("b_cliente_solicitacao_almoxarifado")
            self.click_relative(510, 149)
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
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "ir_solicitacao_almoxarifado", matching=0.97, waiting_time=10000):
                self.not_found("ir_solicitacao_almoxarifado")
            self.click_relative(14, 264)
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
            self.type_keys_with_interval(1,'1')
            if not self.find( "botaoconfirmaritensreqcompras", matching=0.97, waiting_time=10000):
                self.not_found("botaoconfirmaritensreqcompras")
            self.click()
            self.wait(3000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.wait(2000)
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

                            ####---INVENTÁRIO---####

            if not self.find( "estoque4.1", matching=0.97, waiting_time=10000):
                self.not_found("estoque4.1")
            self.click()
            if not self.find( "inventario_estoque", matching=0.97, waiting_time=10000):
                self.not_found("inventario_estoque")
            self.click()
            if not self.find( "selecao_solicitacao_almoxarifado", matching=0.97, waiting_time=10000):
                self.not_found("selecao_solicitacao_almoxarifado")
            self.click()
            if not self.find( "b_item_inventario_estoque", matching=0.97, waiting_time=10000):
                self.not_found("b_item_inventario_estoque")
            self.click_relative(73, 168)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.wait(500)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.tab()
            self.tab()
            self.tab()
            self.type_down()
            self.type_up()
            self.type_up()
            self.type_down()
            self.tab()
            x=0
            while x<4:
                self.type_down()
                x=x+1
            x=0
            while x<4:
                self.type_up()
                x=x+1
            self.tab()
            self.type_down()
            self.type_up()
            self.tab()
            x=0
            while x<5:
                self.type_down()
                x=x+1
            x=0
            while x<5:
                self.type_up()
                x=x+1
            self.tab()
            if not self.find( "b_codigoclientefornecedor_inventario_estoque", matching=0.97, waiting_time=10000):
                self.not_found("b_codigoclientefornecedor_inventario_estoque")
            self.click_relative(80, 238)
            self.enter()
            x=0
            while x<18:
                self.type_down()
                x=x+1
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_operacaoentrada_inventario_estoque", matching=0.97, waiting_time=10000):
                self.not_found("b_operacaoentrada_inventario_estoque")
            self.click_relative(82, 279)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_operacaosaida_inventario_estoque", matching=0.97, waiting_time=10000):
                self.not_found("b_operacaosaida_inventario_estoque")
            self.click_relative(82, 320)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_localestoque_inventario_estoque", matching=0.97, waiting_time=10000):
                self.not_found("b_localestoque_inventario_estoque")
            self.click_relative(541, 280)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            self.tab()
            self.tab()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "a2_inventario_estoque", matching=0.97, waiting_time=10000):
                self.not_found("a2_inventario_estoque")
            self.click()
            if not self.find( "ir_a2p1_inventario_estoque", matching=0.97, waiting_time=10000):
                self.not_found("ir_a2p1_inventario_estoque")
            self.click_relative(18, 164)
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
            self.enter()
            self.space()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            if not self.find( "a2p2_inventario_estoque", matching=0.97, waiting_time=10000):
                self.not_found("a2p2_inventario_estoque")
            self.click()
            if not self.find( "ir_a2p2_inventario_estoque", matching=0.97, waiting_time=10000):
                self.not_found("ir_a2p2_inventario_estoque")
            self.click_relative(19, 165)
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
            if not self.find( "b_clientefornecedor_a2p2_inventario_estoque", matching=0.97, waiting_time=10000):
                self.not_found("b_clientefornecedor_a2p2_inventario_estoque")
            self.click_relative(565, 277)
            self.wait(1000)
            self.enter()
            self.wait(1000)
            x=0
            while x<18:
                self.type_down()
                x=x+1
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "botaoconfirmaritensreqcompras", matching=0.97, waiting_time=10000):
                self.not_found("botaoconfirmaritensreqcompras")
            self.click()
            self.wait(3000)
            self.enter()
            self.space()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            if not self.find( "a2p3_inventario_estoque", matching=0.97, waiting_time=10000):
                self.not_found("a2p3_inventario_estoque")
            self.click()
            if not self.find( "b_lancamentoporitem_inventario_estoque", matching=0.97, waiting_time=10000):
                self.not_found("b_lancamentoporitem_inventario_estoque")
            self.click_relative(240, 207)
            self.type_keys_with_interval(1,'104455')
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "a2p4_inventario_estoque", matching=0.97, waiting_time=10000):
                self.not_found("a2p4_inventario_estoque")
            self.click()
            if not self.find( "b_data_a2p4_inventario_estoque", matching=0.97, waiting_time=10000):
                self.not_found("b_data_a2p4_inventario_estoque")
            self.click_relative(352, 201)
            if not self.find( "carregar_dia_a2p4", matching=0.97, waiting_time=10000):
                self.not_found("carregar_dia_a2p4")
            self.click()
            if not self.find( "carregar_dia_atual_a2p4", matching=0.97, waiting_time=10000):
                self.not_found("carregar_dia_atual_a2p4")
            self.click()
            self.tab()
            self.tab()
            self.space()
            self.space()
            self.tab()
            self.space()
            self.space()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.space()
            self.space()
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
            self.space()
            self.space()
            if not self.find( "filtro_a2p4_inventario_estoque", matching=0.97, waiting_time=10000):
                self.not_found("filtro_a2p4_inventario_estoque")
            self.click()
            if not self.find( "retornar_filtro_a2p4", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtro_a2p4")
            self.click_relative(39, 40)
            if not self.find( "a3_inventario_estoque", matching=0.97, waiting_time=10000):
                self.not_found("a3_inventario_estoque")
            self.click()
            self.tab()
            if not self.find( "a3_filtro_inventario_estoque", matching=0.97, waiting_time=10000):
                self.not_found("a3_filtro_inventario_estoque")
            self.click_relative(52, 15)            
            if not self.find( "retornar_filtro_a2p4", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtro_a2p4")
            self.click_relative(39, 40)
            self.tab()
            self.tab()
            self.type_down()
            self.type_up()
            self.tab()
            x=0
            while x<6:
                self.type_down()
                x=x+1
            x=0
            while x<6:
                self.type_up()
                x=x+1
            self.tab()
            self.space()
            self.space()
            if not self.find( "a4_inventario_estoque", matching=0.97, waiting_time=10000):
                self.not_found("a4_inventario_estoque")
            self.click()
            self.tab()
            self.tab()
            x=0
            while x<4:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            if not self.find( "apagardescricao_inventario_estoque", matching=0.97, waiting_time=10000):
                self.not_found("apagardescricao_inventario_estoque")
            self.click_relative(145, 88)
            x=0
            while x<6:
                self.backspace()
                x=x+1
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
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
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---MANIFESTACAO DO DESTINATARIO---####

            if not self.find( "estoque4.1", matching=0.97, waiting_time=10000):
                self.not_found("estoque4.1")
            self.click()
            if not self.find( "manifestacaododestinatario", matching=0.97, waiting_time=10000):
                self.not_found("manifestacaododestinatario")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            x=0
            while x<3:
                self.type_down()
                x=x+1
            x=0
            while x<3:
                self.type_up()
                x=x+1
            self.tab()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---TRANSFORMACAO ITENS---#### 
                                       
            if not self.find( "estoque4.1", matching=0.97, waiting_time=10000):
                self.not_found("estoque4.1")
            self.click()
            if not self.find( "transformacaodeitens", matching=0.97, waiting_time=10000):
                self.not_found("transformacaodeitens")
            self.click()
            self.wait(1000)
            self.enter()
            if not self.find( "selecao_trans_itens", matching=0.97, waiting_time=10000):
                self.not_found("selecao_trans_itens")
            self.click()
            if not self.find( "b_item_trans_itens", matching=0.97, waiting_time=10000):
                self.not_found("b_item_trans_itens")
            self.click_relative(229, 154)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_clientepedido_trans_itens", matching=0.97, waiting_time=10000):
                self.not_found("b_clientepedido_trans_itens")
            self.click_relative(69, 204)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            x=0
            while x<7:
                self.tab()
                x=x+1
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "ir_itens_trans_itens", matching=0.97, waiting_time=10000):
                self.not_found("ir_itens_trans_itens")
            self.click_relative(17, 271)
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
            self.type_keys_with_interval(1,'1')
            if not self.find( "botaoconfirmaritensreqcompras", matching=0.97, waiting_time=10000):
                self.not_found("botaoconfirmaritensreqcompras")
            self.click()
            self.wait(3000) 
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'1')
            self.tab()
            self.type_keys_with_interval(1,'123')
            #if not self.find( "b_lotenumero_MI_estoque", matching=0.97, waiting_time=10000):
            #    self.not_found("b_lotenumero_MI_estoque")
            #self.click_relative(207, 194)
            #if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
            #    self.not_found("selecionarmunicipiovcr")
            #self.click()
            self.wait(500)
            if not self.find( "b_lotenumero_inf_entradalote_2", matching=0.97, waiting_time=10000):
                self.not_found("b_lotenumero_inf_entradalote_2")
            self.click_relative(206, 148)
            self.backspace()
            self.type_keys_with_interval(1,'123')
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            self.wait(4000)
            #if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
            #    self.not_found("retornarpe")
            #self.click()
            self.key_esc()
            self.wait(4000)
            self.enter()
            self.wait(4000)
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.wait(2000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.wait(2000)
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
            
                            ####---CADASTROS MODO DE TRANSFERENCIAS---####
                             
            if not self.find( "estoque4.1", matching=0.97, waiting_time=10000):
                self.not_found("estoque4.1")
            self.click()
            if not self.find( "transferencias_estoque", matching=0.97, waiting_time=10000):
                self.not_found("transferencias_estoque")
            self.click()
            if not self.find( "cadastros_modotransferencia_estoque", matching=0.97, waiting_time=10000):
                self.not_found("cadastros_modotransferencia_estoque")
            self.click()
            self.backspace()
            self.enter()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "b_origem_empresa_modotrans", matching=0.97, waiting_time=10000):
                self.not_found("b_origem_empresa_modotrans")
            self.click_relative(153, 143)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_origem_empresa_modotrans", matching=0.97, waiting_time=10000):
                self.not_found("b_origem_empresa_modotrans")
            self.click_relative(153, 173)
            self.enter()
            x=0
            while x<18:
                self.type_down()
                x=x+1
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_origem_empresa_modotrans", matching=0.97, waiting_time=10000):
                self.not_found("b_origem_empresa_modotrans")
            self.click_relative(153, 203)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_origem_empresa_modotrans", matching=0.97, waiting_time=10000):
                self.not_found("b_origem_empresa_modotrans")
            self.click_relative(153, 293)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_origem_empresa_modotrans", matching=0.97, waiting_time=10000):
                self.not_found("b_origem_empresa_modotrans")
            self.click_relative(153, 313)
            self.enter()
            x=0
            while x<18:
                self.type_down()
                x=x+1
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_origem_empresa_modotrans", matching=0.97, waiting_time=10000):
                self.not_found("b_origem_empresa_modotrans")
            self.click_relative(153, 333)
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
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "codigo_teste_modotrans", matching=0.97, waiting_time=10000):
                self.not_found("codigo_teste_modotrans")
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
            
                            ####---MOVIMENTO TRANSFERENCIA---####
                             
            if not self.find( "estoque4.1", matching=0.97, waiting_time=10000):
                self.not_found("estoque4.1")
            self.click()
            if not self.find( "transferencias_estoque", matching=0.97, waiting_time=10000):
                self.not_found("transferencias_estoque")
            self.click()
            if not self.find( "movimentodetransferencia_estq", matching=0.97, waiting_time=10000):
                self.not_found("movimentodetransferencia_estq")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            if not self.find( "b_modotransferencia_estoque", matching=0.97, waiting_time=10000):
                self.not_found("b_modotransferencia_estoque")
            self.click_relative(80, 156)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500) 
            if not self.find( "b_vendedor_movtransitens", matching=0.97, waiting_time=10000):
                self.not_found("b_vendedor_movtransitens")
            self.click_relative(82, 246)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500) 
            if not self.find( "b_condpag_movtransitens", matching=0.97, waiting_time=10000):
                self.not_found("b_condpag_movtransitens")
            self.click_relative(82, 290)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500) 
            self.tab()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "ir_movtransitens", matching=0.97, waiting_time=10000):
                self.not_found("ir_movtransitens")
            self.click_relative(17, 317)
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
            self.type_keys_with_interval(1,'1')
            self.tab()
            self.type_keys_with_interval(1,'7')
            self.tab()
            if not self.find( "botaoconfirmaritensreqcompras", matching=0.97, waiting_time=10000):
                self.not_found("botaoconfirmaritensreqcompras")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'1')
            self.tab()
            self.type_keys_with_interval(1,'123')
            if not self.find( "b_numerolote_movtransitens", matching=0.97, waiting_time=10000):
                self.not_found("b_numerolote_movtransitens")
            self.click_relative(204, 193)
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
            self.wait(2000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.wait(2000)
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.wait(2000)
            if not self.find( "op_todas_consultaTransItens", matching=0.97, waiting_time=10000):
                self.not_found("op_todas_consultaTransItens")
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
            
                            ####---DEVOLUCOES CLIENTES---####
                             
            if not self.find( "estoque4.1", matching=0.97, waiting_time=10000):
                self.not_found("estoque4.1")
            self.click()
            if not self.find( "devolucoesclientes_estoque", matching=0.97, waiting_time=10000):
                self.not_found("devolucoesclientes_estoque")
            self.click()
            if not self.find( "aba2_consultadevolucaoitens", matching=0.97, waiting_time=10000):
                self.not_found("aba2_consultadevolucaoitens")
            self.click()
            if not self.find( "b_operacao_devitens", matching=0.97, waiting_time=10000):
                self.not_found("b_operacao_devitens")
            self.click_relative(72, 151)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_condpagamento_devitens", matching=0.97, waiting_time=10000):
                self.not_found("b_condpagamento_devitens")
            self.click_relative(71, 190)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_itens_devitens", matching=0.97, waiting_time=10000):
                self.not_found("b_itens_devitens")
            self.click_relative(71, 226)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_vendedor_devitens", matching=0.97, waiting_time=10000):
                self.not_found("b_vendedor_devitens")
            self.click_relative(460, 188)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            if not self.find( "b_operacao_devitens_pdv", matching=0.97, waiting_time=10000):
                self.not_found("b_operacao_devitens_pdv")
            self.click_relative(83, 149)
            self.backspace()
            self.type_keys_with_interval(1,'0014')
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_vendedor_devitens_pdv", matching=0.97, waiting_time=10000):
                self.not_found("b_vendedor_devitens_pdv")
            self.click_relative(83, 193)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_condpagamento_devitens_pdv", matching=0.97, waiting_time=10000):
                self.not_found("b_condpagamento_devitens_pdv")
            self.click_relative(84, 237)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "b_clientefornecedor_devitens_pdv", matching=0.97, waiting_time=10000):
                self.not_found("b_clientefornecedor_devitens_pdv")
            self.click_relative(482, 149)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "ir_devitens_pdv", matching=0.97, waiting_time=10000):
                self.not_found("ir_devitens_pdv")
            self.click_relative(17, 311)
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
            self.type_keys_with_interval(1,'1')
            self.tab()
            if not self.find( "botaoconfirmaritensreqcompras", matching=0.97, waiting_time=10000):
                self.not_found("botaoconfirmaritensreqcompras")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'1')
            self.tab()
            self.type_keys_with_interval(1,'123')
            if not self.find( "b_lotenumero_inf_entradalote", matching=0.97, waiting_time=10000):
                self.not_found("b_lotenumero_inf_entradalote")
            self.double_click_relative(46, 150)
            self.backspace()
            self.type_keys_with_interval(1,'123')
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.wait(2000)
            self.enter()
            self.wait(4000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.wait(2000)
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.wait(2000)
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
            
                            ####---FICHA CONTEUDO IMPORTACAO---####
                             
            if not self.find( "estoque4.1", matching=0.97, waiting_time=10000):
                self.not_found("estoque4.1")
            self.click()
            if not self.find( "FCI_estoque", matching=0.97, waiting_time=10000):
                self.not_found("FCI_estoque")
            self.click()
            self.enter()
            if not self.find( "ir_movimentoFCI", matching=0.97, waiting_time=10000):
                self.not_found("ir_movimentoFCI")
            self.click_relative(15, 334)
            x=0
            while x<12:
                self.type_down()
                x=x+1
            self.tab()
            x=0
            while x<4:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "gravar_movimentofci", matching=0.97, waiting_time=10000):
                self.not_found("gravar_movimentofci")
            self.click()
            if not self.find( "cancelar_movimentoFCI", matching=0.97, waiting_time=10000):
                self.not_found("cancelar_movimentoFCI")
            self.click()
        
            if not self.find( "deletar_ir_movimentofci", matching=0.97, waiting_time=10000):
                self.not_found("deletar_ir_movimentofci")
            self.click_relative(13, 358)
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














































































































































































