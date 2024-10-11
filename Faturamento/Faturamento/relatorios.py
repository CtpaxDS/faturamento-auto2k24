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

            """self.backspace()
            self.tab()
            self.type_keys_with_interval(1,"Ictus produtos")
            self.enter()"""

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
            self.type_down()
            if not self.find( "relatoriosCadastros", matching=0.97, waiting_time=10000):
                self.not_found("relatoriosCadastros")
            self.click()
            if not self.find( "r_classificacao", matching=0.97, waiting_time=10000):
                self.not_found("r_classificacao")
            self.click()
            self.tab()
            self.type_right()
            self.type_left()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R CENTRO CUSTO---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "relatoriosCadastros", matching=0.97, waiting_time=10000):
                self.not_found("relatoriosCadastros")
            self.click()
            if not self.find( "r_centrosCusto", matching=0.97, waiting_time=10000):
                self.not_found("r_centrosCusto")
            self.click()
            self.tab()
            self.type_right()
            self.type_left()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R COMISSOES---####
            
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "relatoriosCadastros", matching=0.97, waiting_time=10000):
                self.not_found("relatoriosCadastros")
            self.click() 
            if not self.find( "r_comissoes", matching=0.97, waiting_time=10000):
                self.not_found("r_comissoes")
            self.click()
            self.tab()
            self.type_right()
            self.type_left()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R CLIENTES, FORNECEDORES---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "relatoriosCadastros", matching=0.97, waiting_time=10000):
                self.not_found("relatoriosCadastros")
            self.click() 
            if not self.find( "r_clientesFornecedores", matching=0.97, waiting_time=10000):
                self.not_found("r_clientesFornecedores")
            self.click()
            self.tab()
            self.type_down()
            self.type_down()
            self.tab()
            self.type_up()
            self.type_up()
            self.tab()
            self.type_up()
            self.type_up()
            self.tab()
            x=0
            while x<10:
                self.type_left()
                x=x+1
            if not self.find( "b_pais_r_cadastroGeral", matching=0.97, waiting_time=10000):
                self.not_found("b_pais_r_cadastroGeral")
            self.click_relative(191, 195)
            self.type_down()
            self.enter()
            if not self.find( "b_regiao_r_cadastroGeral", matching=0.97, waiting_time=10000):
                self.not_found("b_regiao_r_cadastroGeral")
            self.click_relative(390, 194)
            self.type_down()
            self.enter()
            if not self.find( "b_estado_r_cadastroGeral", matching=0.97, waiting_time=10000):
                self.not_found("b_estado_r_cadastroGeral")
            self.click_relative(590, 195)
            self.type_down()
            self.enter()
            if not self.find( "b_municipio_r_cadastroGeral", matching=0.97, waiting_time=10000):
                self.not_found("b_municipio_r_cadastroGeral")
            self.click_relative(789, 196)
            self.type_down()
            self.enter()
            self.tab()
            self.type_left()
            self.tab()
            self.type_right()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            if not self.find( "data", matching=0.97, waiting_time=10000):
                self.not_found("data")
            self.click_relative(33, 7)
            if not self.find( "data_ano", matching=0.97, waiting_time=10000):
                self.not_found("data_ano")
            self.click()
            if not self.find( "data_ano_anterior", matching=0.97, waiting_time=10000):
                self.not_found("data_ano_anterior")
            self.click()
            self.tab()
            self.type_right()
            self.tab()
            self.type_right()
            self.tab()
            if not self.find( "op_relacionar_r_cadastroGeral", matching=0.97, waiting_time=10000):
                self.not_found("op_relacionar_r_cadastroGeral")
            self.click_relative(20, 282)
            x=0
            while x<6:
                self.type_right()
                x=x+1
            if not self.find( "op_moqu_r_cadastroGeral", matching=0.97, waiting_time=10000):
                self.not_found("op_moqu_r_cadastroGeral")
            self.click_relative(436, 280)
            x=0
            while x<9:
                self.type_right()
                x=x+1
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R CLIENTES VENDEDORES USUARIO---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "relatoriosCadastros", matching=0.97, waiting_time=10000):
                self.not_found("relatoriosCadastros")
            self.click() 
            if not self.find( "R_clientesVendedoresXUsuarios", matching=0.97, waiting_time=10000):
                self.not_found("R_clientesVendedoresXUsuarios")
            self.click()
            self.tab()
            self.type_right()
            self.type_left()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R VENDEDORES E COMPRADORES---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "relatoriosCadastros", matching=0.97, waiting_time=10000):
                self.not_found("relatoriosCadastros")
            self.click() 
            if not self.find( "r_vendedoresECompradores", matching=0.97, waiting_time=10000):
                self.not_found("r_vendedoresECompradores")
            self.click()
            self.tab()
            self.type_right()
            self.type_right()
            if not self.find( "op_listar_RcompradoresVendedores", matching=0.97, waiting_time=10000):
                self.not_found("op_listar_RcompradoresVendedores")
            self.click_relative(20, 123)
            self.type_right()
            self.type_right()
            self.tab()
            if not self.find( "op_ordemImpressao_rCompradoresVendedores", matching=0.97, waiting_time=10000):
                self.not_found("op_ordemImpressao_rCompradoresVendedores")
            self.click_relative(523, 112)
            self.type_right()
            self.type_right()
            self.type_right()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R CONDICOES DE PAGAMENTO---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "relatoriosCadastros", matching=0.97, waiting_time=10000):
                self.not_found("relatoriosCadastros")
            self.click() 
            if not self.find( "r_condicoesPagamento", matching=0.97, waiting_time=10000):
                self.not_found("r_condicoesPagamento")
            self.click()
            self.tab()
            self.type_right()
            self.type_left()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R EMPRESAS---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "relatoriosCadastros", matching=0.97, waiting_time=10000):
                self.not_found("relatoriosCadastros")
            self.click() 
            if not self.find( "r_empresas", matching=0.97, waiting_time=10000):
                self.not_found("r_empresas")
            self.click()
            self.tab()
            self.type_right()
            self.type_left()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R GRUPO DE EMPRESAS---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "relatoriosCadastros", matching=0.97, waiting_time=10000):
                self.not_found("relatoriosCadastros")
            self.click() 
            if not self.find( "r_grupoDeEmpresas", matching=0.97, waiting_time=10000):
                self.not_found("r_grupoDeEmpresas")
            self.click()
            self.tab()
            self.type_right()
            self.type_left()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R PF REG PAISES---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "relatoriosCadastros", matching=0.97, waiting_time=10000):
                self.not_found("relatoriosCadastros")
            self.click() 
            if not self.find( "r_ParametrosFiscais", matching=0.97, waiting_time=10000):
                self.not_found("r_ParametrosFiscais")
            self.click()
            if not self.find( "r_pf_regionalizacao", matching=0.97, waiting_time=10000):
                self.not_found("r_pf_regionalizacao")
            self.click()
            if not self.find( "r_pf_reg_paises", matching=0.97, waiting_time=10000):
                self.not_found("r_pf_reg_paises")
            self.click()
            self.tab()
            self.type_right()
            self.type_left()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R PF REG REGIOES---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "relatoriosCadastros", matching=0.97, waiting_time=10000):
                self.not_found("relatoriosCadastros")
            self.click() 
            if not self.find( "r_ParametrosFiscais", matching=0.97, waiting_time=10000):
                self.not_found("r_ParametrosFiscais")
            self.click()
            if not self.find( "r_pf_regionalizacao", matching=0.97, waiting_time=10000):
                self.not_found("r_pf_regionalizacao")
            self.click()
            if not self.find( "r_pf_reg_regioes", matching=0.97, waiting_time=10000):
                self.not_found("r_pf_reg_regioes")
            self.click()
            self.tab()
            self.type_right()
            self.type_left()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R PF REG ESTADOS---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "relatoriosCadastros", matching=0.97, waiting_time=10000):
                self.not_found("relatoriosCadastros")
            self.click() 
            if not self.find( "r_ParametrosFiscais", matching=0.97, waiting_time=10000):
                self.not_found("r_ParametrosFiscais")
            self.click()
            if not self.find( "r_pf_regionalizacao", matching=0.97, waiting_time=10000):
                self.not_found("r_pf_regionalizacao")
            self.click()
            if not self.find( "r_pf_reg_estados", matching=0.97, waiting_time=10000):
                self.not_found("r_pf_reg_estados")
            self.click()
            self.tab()
            self.type_right()
            self.type_left()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R PF REG MUNICIPIOS---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "relatoriosCadastros", matching=0.97, waiting_time=10000):
                self.not_found("relatoriosCadastros")
            self.click() 
            if not self.find( "r_ParametrosFiscais", matching=0.97, waiting_time=10000):
                self.not_found("r_ParametrosFiscais")
            self.click()
            if not self.find( "r_pf_regionalizacao", matching=0.97, waiting_time=10000):
                self.not_found("r_pf_regionalizacao")
            self.click()
            if not self.find( "r_pf_reg_municipios", matching=0.97, waiting_time=10000):
                self.not_found("r_pf_reg_municipios")
            self.click()
            self.tab()
            self.type_right()
            self.type_left()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R ITENS AGR FAMILIA---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "relatoriosCadastros", matching=0.97, waiting_time=10000):
                self.not_found("relatoriosCadastros")
            self.click() 
            if not self.find( "r_itensEstoque", matching=0.97, waiting_time=10000):
                self.not_found("r_itensEstoque")
            self.click()
            if not self.find( "r_itensEstoque_agrupamento", matching=0.97, waiting_time=10000):
                self.not_found("r_itensEstoque_agrupamento")
            self.click()
            if not self.find( "r_itens_agr_familia", matching=0.97, waiting_time=10000):
                self.not_found("r_itens_agr_familia")
            self.click()
            self.tab()
            self.type_right()
            self.type_left()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R ITENS AGR GRUPOS---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "relatoriosCadastros", matching=0.97, waiting_time=10000):
                self.not_found("relatoriosCadastros")
            self.click() 
            if not self.find( "r_itensEstoque", matching=0.97, waiting_time=10000):
                self.not_found("r_itensEstoque")
            self.click()
            if not self.find( "r_itensEstoque_agrupamento", matching=0.97, waiting_time=10000):
                self.not_found("r_itensEstoque_agrupamento")
            self.click()
            if not self.find( "r_itens_agr_grupos", matching=0.97, waiting_time=10000):
                self.not_found("r_itens_agr_grupos")
            self.click()
            self.tab()
            self.type_right()
            self.type_left()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R ITENS AGR SUBGRUPOS---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "relatoriosCadastros", matching=0.97, waiting_time=10000):
                self.not_found("relatoriosCadastros")
            self.click() 
            if not self.find( "r_itensEstoque", matching=0.97, waiting_time=10000):
                self.not_found("r_itensEstoque")
            self.click()
            if not self.find( "r_itensEstoque_agrupamento", matching=0.97, waiting_time=10000):
                self.not_found("r_itensEstoque_agrupamento")
            self.click()
            if not self.find( "r_itens_agr_subGrupos", matching=0.97, waiting_time=10000):
                self.not_found("r_itens_agr_subGrupos")
            self.click()
            self.tab()
            self.type_right()
            self.type_left()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R ITENS AGR MARCAS---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "relatoriosCadastros", matching=0.97, waiting_time=10000):
                self.not_found("relatoriosCadastros")
            self.click() 
            if not self.find( "r_itensEstoque", matching=0.97, waiting_time=10000):
                self.not_found("r_itensEstoque")
            self.click()
            if not self.find( "r_itensEstoque_agrupamento", matching=0.97, waiting_time=10000):
                self.not_found("r_itensEstoque_agrupamento")
            self.click()
            if not self.find( "r_itens_agr_marcas", matching=0.97, waiting_time=10000):
                self.not_found("r_itens_agr_marcas")
            self.click()
            self.tab()
            self.type_right()
            self.type_left()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R ITENS AGR UNIDADES---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "relatoriosCadastros", matching=0.97, waiting_time=10000):
                self.not_found("relatoriosCadastros")
            self.click() 
            if not self.find( "r_itensEstoque", matching=0.97, waiting_time=10000):
                self.not_found("r_itensEstoque")
            self.click()
            if not self.find( "r_itensEstoque_agrupamento", matching=0.97, waiting_time=10000):
                self.not_found("r_itensEstoque_agrupamento")
            self.click()
            if not self.find( "r_itens_agr_unidades", matching=0.97, waiting_time=10000):
                self.not_found("r_itens_agr_unidades")
            self.click()
            self.tab()
            self.type_right()
            self.type_left()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R ITENS AGR TIPOS---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "relatoriosCadastros", matching=0.97, waiting_time=10000):
                self.not_found("relatoriosCadastros")
            self.click() 
            if not self.find( "r_itensEstoque", matching=0.97, waiting_time=10000):
                self.not_found("r_itensEstoque")
            self.click()
            if not self.find( "r_itensEstoque_agrupamento", matching=0.97, waiting_time=10000):
                self.not_found("r_itensEstoque_agrupamento")
            self.click()    
            if not self.find( "r_itens_agr_tipos", matching=0.97, waiting_time=10000):
                self.not_found("r_itens_agr_tipos")
            self.click()
            self.tab()
            self.type_right()
            self.type_left()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R ITENS AGR SUBTIPOS---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "relatoriosCadastros", matching=0.97, waiting_time=10000):
                self.not_found("relatoriosCadastros")
            self.click() 
            if not self.find( "r_itensEstoque", matching=0.97, waiting_time=10000):
                self.not_found("r_itensEstoque")
            self.click()
            if not self.find( "r_itensEstoque_agrupamento", matching=0.97, waiting_time=10000):
                self.not_found("r_itensEstoque_agrupamento")
            self.click()   
            if not self.find( "r_itens_agr_subTipos", matching=0.97, waiting_time=10000):
                self.not_found("r_itens_agr_subTipos")
            self.click()
            self.tab()
            self.type_right()
            self.type_left()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R ITENS AGR CONTROLES---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "relatoriosCadastros", matching=0.97, waiting_time=10000):
                self.not_found("relatoriosCadastros")
            self.click() 
            if not self.find( "r_itensEstoque", matching=0.97, waiting_time=10000):
                self.not_found("r_itensEstoque")
            self.click()
            if not self.find( "r_itensEstoque_agrupamento", matching=0.97, waiting_time=10000):
                self.not_found("r_itensEstoque_agrupamento")
            self.click()   
            if not self.find( "r_itens_agr_controles", matching=0.97, waiting_time=10000):
                self.not_found("r_itens_agr_controles")
            self.click()
            self.tab()
            self.type_right()
            self.type_left()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R ITENS ITENS---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "relatoriosCadastros", matching=0.97, waiting_time=10000):
                self.not_found("relatoriosCadastros")
            self.click() 
            if not self.find( "r_itensEstoque", matching=0.97, waiting_time=10000):
                self.not_found("r_itensEstoque")
            self.click()
            if not self.find( "r_itens_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_itens_itens")
            self.click()
            if not self.find( "op_itens_codImprimir", matching=0.97, waiting_time=10000):
                self.not_found("op_itens_codImprimir")
            self.click_relative(18, 113)
            self.type_right()
            self.type_right()
            self.type_right()
            if not self.find( "op_itens_agruparPor", matching=0.97, waiting_time=10000):
                self.not_found("op_itens_agruparPor")
            self.click_relative(16, 159)
            self.type_right()
            self.type_right()
            self.type_right()
            if not self.find( "op_itens_situacao", matching=0.97, waiting_time=10000):
                self.not_found("op_itens_situacao")
            self.click_relative(19, 215)
            self.type_right()
            self.type_right()
            if not self.find( "op_itens_imprimirPesos", matching=0.97, waiting_time=10000):
                self.not_found("op_itens_imprimirPesos")
            self.click_relative(247, 214)
            self.type_right()
            if not self.find( "op_itens_agrupaFornecedor", matching=0.97, waiting_time=10000):
                self.not_found("op_itens_agrupaFornecedor")
            self.click_relative(348, 216)
            self.type_right()
            if not self.find( "op_itens_valores", matching=0.97, waiting_time=10000):
                self.not_found("op_itens_valores")
            self.click_relative(485, 203)
            self.type_right()
            self.type_right()
            self.type_right()
            if not self.find( "op_itens_marcadosPis", matching=0.97, waiting_time=10000):
                self.not_found("op_itens_marcadosPis")
            self.click_relative(747, 213)
            self.type_right()
            self.type_right()
            if not self.find( "op_itens_ordemImpressao", matching=0.97, waiting_time=10000):
                self.not_found("op_itens_ordemImpressao")
            self.click_relative(19, 272)
            self.type_right()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R ITENS CADEIA DE PRECOS---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "relatoriosCadastros", matching=0.97, waiting_time=10000):
                self.not_found("relatoriosCadastros")
            self.click() 
            if not self.find( "r_itensEstoque", matching=0.97, waiting_time=10000):
                self.not_found("r_itensEstoque")
            self.click()
            if not self.find( "r_itens_cadeiaPrecos", matching=0.97, waiting_time=10000):
                self.not_found("r_itens_cadeiaPrecos")
            self.click()
            self.tab()
            self.type_right()
            self.tab()
            self.type_right()
            self.tab()
            self.type_right()
            self.type_right()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R ITENS LOCAL DE ESTOQUE---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "relatoriosCadastros", matching=0.97, waiting_time=10000):
                self.not_found("relatoriosCadastros")
            self.click() 
            if not self.find( "r_itensEstoque", matching=0.97, waiting_time=10000):
                self.not_found("r_itensEstoque")
            self.click()
            if not self.find( "r_itens_localEstoque", matching=0.97, waiting_time=10000):
                self.not_found("r_itens_localEstoque")
            self.click()
            self.tab()
            self.type_right()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R USUARIOS---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "relatoriosCadastros", matching=0.97, waiting_time=10000):
                self.not_found("relatoriosCadastros")
            self.click() 
            if not self.find( "r_usuarios", matching=0.97, waiting_time=10000):
                self.not_found("r_usuarios")
            self.click()
            self.tab()
            self.type_right()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R PLANO FINANCEIRO---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "relatoriosCadastros", matching=0.97, waiting_time=10000):
                self.not_found("relatoriosCadastros")
            self.click() 
            if not self.find( "r_planoFinanceiro", matching=0.97, waiting_time=10000):
                self.not_found("r_planoFinanceiro")
            self.click()
            self.tab()
            self.type_right()
            self.tab()
            self.type_right()
            self.type_right()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R LOCAL COBRANCA---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "relatoriosCadastros", matching=0.97, waiting_time=10000):
                self.not_found("relatoriosCadastros")
            self.click() 
            if not self.find( "r_localCobranca", matching=0.97, waiting_time=10000):
                self.not_found("r_localCobranca")
            self.click()
            self.tab()
            self.type_right()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R SERVICOS---####
            
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "relatoriosCadastros", matching=0.97, waiting_time=10000):
                self.not_found("relatoriosCadastros")
            self.click()                  
            if not self.find( "r_servicos", matching=0.97, waiting_time=10000):
                self.not_found("r_servicos")
            self.click()
            self.tab()
            self.type_right()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R LINHAS---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "relatoriosCadastros", matching=0.97, waiting_time=10000):
                self.not_found("relatoriosCadastros")
            self.click() 
            if not self.find( "r_linhasRamosETC", matching=0.97, waiting_time=10000):
                self.not_found("r_linhasRamosETC")
            self.click()
            if not self.find( "r_LR_linhas", matching=0.97, waiting_time=10000):
                self.not_found("r_LR_linhas")
            self.click()
            self.tab()
            self.type_right()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R RAMOS ATIVIDADE---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "relatoriosCadastros", matching=0.97, waiting_time=10000):
                self.not_found("relatoriosCadastros")
            self.click() 
            if not self.find( "r_linhasRamosETC", matching=0.97, waiting_time=10000):
                self.not_found("r_linhasRamosETC")
            self.click()
            if not self.find( "r_ramosAtividade", matching=0.97, waiting_time=10000):
                self.not_found("r_ramosAtividade")
            self.click()
            self.tab()
            self.type_right()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R ROTAS ENTREGA---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "relatoriosCadastros", matching=0.97, waiting_time=10000):
                self.not_found("relatoriosCadastros")
            self.click() 
            if not self.find( "r_linhasRamosETC", matching=0.97, waiting_time=10000):
                self.not_found("r_linhasRamosETC")
            self.click()
            if not self.find( "r_rotasEntrega", matching=0.97, waiting_time=10000):
                self.not_found("r_rotasEntrega")
            self.click()
            self.tab()
            self.type_right()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R SEGMENTOS---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "relatoriosCadastros", matching=0.97, waiting_time=10000):
                self.not_found("relatoriosCadastros")
            self.click() 
            if not self.find( "r_linhasRamosETC", matching=0.97, waiting_time=10000):
                self.not_found("r_linhasRamosETC")
            self.click()
            if not self.find( "r_segmentos", matching=0.97, waiting_time=10000):
                self.not_found("r_segmentos")
            self.click()
            self.tab()
            self.type_right()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R TIPOS CONTRATO---####
                             
            #if not self.find( "relatorios", matching=0.97, waiting_time=10000):
            #    self.not_found("relatorios")
            #self.click()
            #self.type_down()
            #self.type_down()
            #if not self.find( "relatoriosCadastros", matching=0.97, waiting_time=10000):
            #    self.not_found("relatoriosCadastros")
            #self.click() 
            #if not self.find( "r_linhasRamosETC", matching=0.97, waiting_time=10000):
            #    self.not_found("r_linhasRamosETC")
            #self.click()
            """
            if not self.find( "r_tiposContrato", matching=0.97, waiting_time=10000):
                self.not_found("r_tiposContrato")
            self.click()
            self.tab()
            self.type_right()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            """
            #if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
            #    self.not_found("retornarpe")
            #self.click()
            
            
                            ####---R CLIENTES CONTATOS---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "relatoriosCadastros", matching=0.97, waiting_time=10000):
                self.not_found("relatoriosCadastros")
            self.click() 
            if not self.find( "r_clientesContatos", matching=0.97, waiting_time=10000):
                self.not_found("r_clientesContatos")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.tab()
            x=0
            while x<13:
                self.type_down()
                x=x+1
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            self.type_right()
            self.tab()
            self.type_right()
            self.type_right()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R TABELAS---####
                             
            """if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "relatoriosCadastros", matching=0.97, waiting_time=10000):
                self.not_found("relatoriosCadastros")
            self.click() 
            if not self.find( "r_tabelas", matching=0.97, waiting_time=10000):
                self.not_found("r_tabelas")
            self.click()
            self.tab()
            self.type_right()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()"""
            
                            ####---R CATEGORIAS---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "relatoriosCadastros", matching=0.97, waiting_time=10000):
                self.not_found("relatoriosCadastros")
            self.click() 
            if not self.find( "r_categorias", matching=0.97, waiting_time=10000):
                self.not_found("r_categorias")
            self.click()
            self.tab()
            self.type_right()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---R MAPA ECONOMICO COTACAO---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_compras", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_compras")
            self.click()
            if not self.find( "r_mapaEconomicoCotacao", matching=0.97, waiting_time=10000):
                self.not_found("r_mapaEconomicoCotacao")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
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
            
                            ####---R MOVIMENTACAO PEDIDO COMPRAS---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_compras", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_compras")
            self.click()
            if not self.find( "r_movimentacaoPedidoCompras", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentacaoPedidoCompras")
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
            self.type_right()
            self.type_right()
            self.tab()
            self.type_right()
            self.tab()
            self.type_right()
            self.type_right()
            self.type_right()
            self.tab()
            self.type_right()
            self.tab()
            x=0
            while x<4:
                y=0
                while y<6:
                    self.type_down()
                    y=y+1
                self.tab()
                x=x+1
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
            
                            ####---R RELACAO PEDIDO COMPRA---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_compras", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_compras")
            self.click()
            if not self.find( "r_relacaoPedidoCompra", matching=0.97, waiting_time=10000):
                self.not_found("r_relacaoPedidoCompra")
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
            self.type_right()
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
            self.tab()
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
            
                            ####---R PEDIDO COMPRA FORNECEDOR---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_compras", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_compras")
            self.click()
            if not self.find( "r_pedidoCompraFornecedor", matching=0.97, waiting_time=10000):
                self.not_found("r_pedidoCompraFornecedor")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            self.type_keys_with_interval(1,'123')
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
            
                            ####---R RELACAO COMPRA ITENS---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_compras", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_compras")
            self.click()
            if not self.find( "r_relacaoCompraItens", matching=0.97, waiting_time=10000):
                self.not_found("r_relacaoCompraItens")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
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
            
                            ####---R COMPRAS SUGESTAO---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_compras", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_compras")
            self.click()
            if not self.find( "r_comprasSugestao", matching=0.97, waiting_time=10000):
                self.not_found("r_comprasSugestao")
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
            
                            ####---R RELACAO COMPRAS PENDENTES---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_compras", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_compras")
            self.click()
            if not self.find( "r_relacaoComprasPendentes", matching=0.97, waiting_time=10000):
                self.not_found("r_relacaoComprasPendentes")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.tab()
            if not self.find( "op_situacoes_RMPC", matching=0.97, waiting_time=10000):
                self.not_found("op_situacoes_RMPC")
            self.click_relative(428, 135)
            x=0
            while x<4:
                self.space()
                self.type_down()
                x=x+1
            self.tab()
            self.space()
            self.space()
            self.tab()
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
            
                            ####---R RELATORIO AUXILIAR TROCAS---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_compras", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_compras")
            self.click()
            if not self.find( "r_relatorioAuxiliarTrocas", matching=0.97, waiting_time=10000):
                self.not_found("r_relatorioAuxiliarTrocas")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
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
            
                            ####---R RELATORIO AGENDAMENTO---####
            
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_compras", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_compras")
            self.click()                 
            if not self.find( "r_relatorioAgendamento", matching=0.97, waiting_time=10000):
                self.not_found("r_relatorioAgendamento")
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
            
                            ####---R PEDIDO COM HISTORICO---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_compras", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_compras")
            self.click()
            if not self.find( "r_pedidoComHistorico", matching=0.97, waiting_time=10000):
                self.not_found("r_pedidoComHistorico")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.tab()
            if not self.find( "b_fornecedor_pedidoCHistorico", matching=0.97, waiting_time=10000):
                self.not_found("b_fornecedor_pedidoCHistorico")
            self.click_relative(72, 127)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.tab()
            self.tab()
            self.tab()
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
            
                            ####---R FORNECEDORES POR ITEM---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_compras", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_compras")
            self.click()
            if not self.find( "r_fornecedoresPorItem", matching=0.97, waiting_time=10000):
                self.not_found("r_fornecedoresPorItem")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            if not self.find( "b_fornecedor_FI", matching=0.97, waiting_time=10000):
                self.not_found("b_fornecedor_FI")
            self.click_relative(72, 128)
            self.enter()
            x=0
            while x<18:
                self.type_down()
                x=x+1
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_item_rFI", matching=0.97, waiting_time=10000):
                self.not_found("b_item_rFI")
            self.click_relative(455, 131)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
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
            
                            ####---R ITENS PRECOS COMPARATIVO---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_compras", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_compras")
            self.click()
            if not self.find( "r_itensPrecosComparativo", matching=0.97, waiting_time=10000):
                self.not_found("r_itensPrecosComparativo")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
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
            
                            ####---R ITENS PRECOS VARIACAO---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_compras", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_compras")
            self.click()
            if not self.find( "r_itensPrecosVariacao", matching=0.97, waiting_time=10000):
                self.not_found("r_itensPrecosVariacao")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.type_right()
            self.type_right()
            self.tab()
            self.type_right()
            self.type_right()
            self.type_right()
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
            
                            ####---R ITENS A COMPRAR---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_compras", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_compras")
            self.click()
            if not self.find( "r_itensAComprar", matching=0.97, waiting_time=10000):
                self.not_found("r_itensAComprar")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.space()
            self.space()
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
            
                            ####---R CONTAS A PAGAR---####
                             
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_financeiro", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_financeiro")
            self.click()
            if not self.find( "r_contasAPagar", matching=0.97, waiting_time=10000):
                self.not_found("r_contasAPagar")
            self.click()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            x=0
            while x<4:
                self.type_right()
                x=x+1
            self.tab()
            x=0
            while x<11:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            x=0
            while x<3:
                self.tab()
                self.space()
                self.space()
                x=x+1
            if not self.find( "b_grupoEmpresa_r_contaspagar", matching=0.97, waiting_time=10000):
                self.not_found("b_grupoEmpresa_r_contaspagar")
            self.click_relative(64, 196)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            self.tab()
            self.tab()
            self.tab()
            self.type_right()
            self.type_right()
            self.type_right()
            self.tab()
            x=0
            while x<5:
                self.type_right()
                x=x+1
            self.tab()
            x=0
            while x<16:
                self.space()
                self.space()
                self.tab()
                x=x+1
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

                            ####---R IMPRESSAO GRAFICA---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_financeiro", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_financeiro")
            self.click()
            if not self.find( "r_contasAPagarIG", matching=0.97, waiting_time=10000):
                self.not_found("r_contasAPagarIG")
            self.click()
            x=0
            while x<3:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
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
            self.type_right()
            self.type_right()
            self.type_right()
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
            if not self.find( "b_grupoEmpresa_r_mfcontaspagar", matching=0.97, waiting_time=10000):
                self.not_found("b_grupoEmpresa_r_mfcontaspagar")
            self.click_relative(64, 183)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            self.tab()
            self.tab()
            self.type_right()
            self.type_right()
            self.type_right()
            self.tab()
            x=0
            while x<18:
                self.type_down()
                x=x+1
            self.tab()
            self.tab()
            self.type_right()
            self.type_right()
            self.type_right()
            self.tab()
            x=0
            while x<5:
                self.type_right()
                x=x+1
            self.tab()
            x=0
            while x<5:
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
            
                            ####---R CONTAS RECEBER---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_financeiro", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_financeiro")
            self.click()
            if not self.find( "r_contasReceber", matching=0.97, waiting_time=10000):
                self.not_found("r_contasReceber")
            self.click()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            x=0
            while x<4:
                self.type_right()
                x=x+1
            self.tab()
            x=0
            while x<11:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            x=0
            while x<3:
                self.tab()
                self.space()
                self.space()
                x=x+1
            if not self.find( "b_grupoEmpresa_r_contasReceber", matching=0.97, waiting_time=10000):
                self.not_found("b_grupoEmpresa_r_contasReceber")
            self.click_relative(64, 197)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            self.tab()
            self.tab()
            self.tab()
            self.type_right()
            self.type_right()
            self.type_right()
            self.tab()
            x=0
            while x<5:
                self.type_right()
                x=x+1
            self.tab()
            x=0
            while x<16:
                self.space()
                self.space()
                self.tab()
                x=x+1
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
            
                            ####---R CONTAS RECEBER IG---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_financeiro", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_financeiro")
            self.click()
            if not self.find( "r_contasReceber_IG", matching=0.97, waiting_time=10000):
                self.not_found("r_contasReceber_IG")
            self.click()
            x=0
            while x<3:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
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
            self.type_right()
            self.type_right()
            self.type_right()
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
            if not self.find( "b_grupoEmpresa_r_mfcontaspagar", matching=0.97, waiting_time=10000):
                self.not_found("b_grupoEmpresa_r_mfcontaspagar")
            self.click_relative(64, 183)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            self.tab()
            self.tab()
            self.type_right()
            self.type_right()
            self.type_right()
            self.tab()
            x=0
            while x<18:
                self.type_down()
                x=x+1
            self.tab()
            self.tab()
            self.type_right()
            self.type_right()
            self.type_right()
            self.tab()
            x=0
            while x<5:
                self.type_right()
                x=x+1
            self.tab()
            x=0
            while x<5:
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

                            ####---R TITULOS BAIXADOS NO PERIODO---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_financeiro", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_financeiro")
            self.click()
            if not self.find( "r_titulosBaixadosNoPeriodo", matching=0.97, waiting_time=10000):
                self.not_found("r_titulosBaixadosNoPeriodo")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "b_grupoEmpresa_r_titulosBaixados", matching=0.97, waiting_time=10000):
                self.not_found("b_grupoEmpresa_r_titulosBaixados")
            self.click_relative(63, 257)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            self.tab()
            self.tab()
            x=0
            while x<7:
                self.type_right()
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

                            ####---R MOVIMENTO FINANCEIRO POR PLANO---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_financeiro", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_financeiro")
            self.click()
            if not self.find( "r_movFinanceiroPlano", matching=0.97, waiting_time=10000):
                self.not_found("r_movFinanceiroPlano")
            self.click()
            x=0
            while x<4:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.type_right()
            self.type_right()
            self.tab()
            x=0
            while x<3:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            if not self.find( "b_grupoEmpresa_r_FplanoF", matching=0.97, waiting_time=10000):
                self.not_found("b_grupoEmpresa_r_FplanoF")
            self.click_relative(62, 205)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            self.tab()
            self.tab()
            x=0
            while x<3:
                self.type_right()
                self.type_right()
                self.tab()
                x=x+1
            x=0
            while x<4:
                self.type_right()
                self.tab()
                x=x+1
            self.tab()
            self.type_right()
            self.type_right()
            self.type_right()
            self.type_right()
            self.tab()
            self.type_right()
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

                            ####---R AUTORIZACAO PAGAMENTO---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_financeiro", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_financeiro")
            self.click()
            if not self.find( "r_autorizacaoPagamento", matching=0.97, waiting_time=10000):
                self.not_found("r_autorizacaoPagamento")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            x=0
            while x<7:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.tab()
            x=0
            while x<4:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            x=0
            while x<5:
                self.type_right()
                self.type_right()
                self.tab()
                x=x+1
            self.space()
            self.space()
            self.tab()
            self.type_right()
            self.tab()
            self.type_right()
            self.tab()
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

                            ####---R FINANCEIRO CENTRO DE CUSTO---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_financeiro", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_financeiro")
            self.click()
            if not self.find( "r_financeiroCentroCusto", matching=0.97, waiting_time=10000):
                self.not_found("r_financeiroCentroCusto")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            x=0
            while x<7:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.tab()
            if not self.find( "b_grupoEmpresa_r_FcentroCusto", matching=0.97, waiting_time=10000):
                self.not_found("b_grupoEmpresa_r_FcentroCusto")
            self.click_relative(61, 127)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            if not self.find( "b_centroCustoInicial_r_FcentroCusto", matching=0.97, waiting_time=10000):
                self.not_found("b_centroCustoInicial_r_FcentroCusto")
            self.click_relative(208, 172)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_centroCustoFinal_r_FcentroCusto", matching=0.97, waiting_time=10000):
                self.not_found("b_centroCustoFinal_r_FcentroCusto")
            self.click_relative(211, 200)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.tab()
            self.type_right()
            self.type_right()
            self.type_right()
            self.tab()
            self.type_right()
            self.tab()
            self.type_up()
            self.type_down()
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            self.space()
            self.space()
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
            
                            ####---R RELACAO REMESSA BANCARIA---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_financeiro", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_financeiro")
            self.click()
            if not self.find( "r_relacaoRemessaBancaria", matching=0.97, waiting_time=10000):
                self.not_found("r_relacaoRemessaBancaria")
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
            self.type_keys_with_interval(1,'123')
            self.tab()
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
            self.type_right()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            if not self.find( "b_bancos_r_remessaBancaria", matching=0.97, waiting_time=10000):
                self.not_found("b_bancos_r_remessaBancaria")
            self.click_relative(64, 187)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.tab()
            self.tab()
            self.type_down()
            self.type_down()
            self.enter()
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

                            ####---R MOVIMENTOS TITULOS PLANO---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_financeiro", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_financeiro")
            self.click()
            if not self.find( "r_movimentoTitulosPlano", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentoTitulosPlano")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            self.tab()
            self.tab()
            self.tab()
            x=0
            while x<4:
                self.type_right()
                self.type_right()
                self.tab()
                x=x+1
            if not self.find( "b_grupoEmpresa_r_receitaXDespesa", matching=0.97, waiting_time=10000):
                self.not_found("b_grupoEmpresa_r_receitaXDespesa")
            self.click_relative(68, 211)
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

                            ####---R BAIXAS E MOV ENCONTRO DE CONTAS---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_financeiro", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_financeiro")
            self.click()
            if not self.find( "r_baixasMovimentoEncontro", matching=0.97, waiting_time=10000):
                self.not_found("r_baixasMovimentoEncontro")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.tab()
            if not self.find( "b_grupoEmpresa_r_encontroContas", matching=0.97, waiting_time=10000):
                self.not_found("b_grupoEmpresa_r_encontroContas")
            self.click_relative(63, 127)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            self.tab()
            self.tab()
            self.tab()
            x=0
            while x<4:
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

                            ####---R FLUXO DE CAIXA---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_financeiro", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_financeiro")
            self.click()
            if not self.find( "r_fluxoCaixa", matching=0.97, waiting_time=10000):
                self.not_found("r_fluxoCaixa")
            self.click()
            x=0
            while x<5:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.tab()
            x=0
            while x<6:
                self.type_right()
                self.tab()
                x=x+1
            if not self.find( "b_grupoEmpresa_r_fluxoCaixa", matching=0.97, waiting_time=10000):
                self.not_found("b_grupoEmpresa_r_fluxoCaixa")
            self.click_relative(43, 210)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            self.tab()
            self.tab()
            self.space()
            self.space()
            self.tab()
            if not self.find( "op_tipoR1_r_FC", matching=0.97, waiting_time=10000):
                self.not_found("op_tipoR1_r_FC")
            self.click_relative(-1, 169)
            self.type_right()
            if not self.find( "op_saldoInicial_r_FC", matching=0.97, waiting_time=10000):
                self.not_found("op_saldoInicial_r_FC")
            self.click_relative(105, 147)
            self.type_right()
            self.type_right()
            if not self.find( "op_tipoR2_r_FC", matching=0.97, waiting_time=10000):
                self.not_found("op_tipoR2_r_FC")
            self.click_relative(243, 151)
            self.type_right()
            if not self.find( "op_saldoAnterior_r_FC", matching=0.97, waiting_time=10000):
                self.not_found("op_saldoAnterior_r_FC")
            self.click_relative(352, 151)
            self.type_right()
            if not self.find( "op_chequeRecebido_r_FC", matching=0.97, waiting_time=10000):
                self.not_found("op_chequeRecebido_r_FC")
            self.click_relative(459, 153)
            self.type_right()
            if not self.find( "op_chequeEmitido_r_FC", matching=0.97, waiting_time=10000):
                self.not_found("op_chequeEmitido_r_FC")
            self.click_relative(568, 150)
            self.type_right()
            if not self.find( "op_lancEfetivos_r_FC", matching=0.97, waiting_time=10000):
                self.not_found("op_lancEfetivos_r_FC")
            self.click_relative(675, 151)
            self.type_right()
            self.type_right()
            if not self.find( "op_checagem_r_FC", matching=0.97, waiting_time=10000):
                self.not_found("op_checagem_r_FC")
            self.click_relative(788, 150)
            self.type_right()
            if not self.find( "op_DuplicataDesc_r_FC", matching=0.97, waiting_time=10000):
                self.not_found("op_DuplicataDesc_r_FC")
            self.click_relative(0, 263)
            self.type_right()
            if not self.find( "op_pedidoCompra_r_FC", matching=0.97, waiting_time=10000):
                self.not_found("op_pedidoCompra_r_FC")
            self.click_relative(197, 264)
            self.type_right()
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()

                            ####---R FC PLANO FINANCEIRO DIARIO---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_financeiro", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_financeiro")
            self.click()
            if not self.find( "r_FCPlanoFinanceiro", matching=0.97, waiting_time=10000):
                self.not_found("r_FCPlanoFinanceiro")
            self.click()
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
            if not self.find( "b_pFinanceiroInicial_r_FPF", matching=0.97, waiting_time=10000):
                self.not_found("b_pFinanceiroInicial_r_FPF")
            self.click_relative(191, 226)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_pFinanceiroFinal_r_FPF", matching=0.97, waiting_time=10000):
                self.not_found("b_pFinanceiroFinal_r_FPF")
            self.click_relative(192, 251)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.tab()
            x=0
            while x<3:
                self.space()
                self.space()
                self.tab()
                x=x+1
            self.tab()
            self.type_up()
            self.type_down()
            x=0
            while x<2:
                self.space()
                self.space()
                self.tab()
                x=x+1
            if not self.find( "informacoes_claro", matching=0.97, waiting_time=10000):
                self.not_found("informacoes_claro")
            self.click()
            if not self.find( "ok_informacoes", matching=0.97, waiting_time=10000):
                self.not_found("ok_informacoes")
            self.click()
            if not self.find( "retornar_claro", matching=0.97, waiting_time=10000):
                self.not_found("retornar_claro")
            self.click()
            
                            ####---R FC MOVTO DE CONTAS---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_financeiro", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_financeiro")
            self.click()
            if not self.find( "r_FCMovtoContas", matching=0.97, waiting_time=10000):
                self.not_found("r_FCMovtoContas")
            self.click()
            x=0
            while x<3:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.type_right()
            self.tab()
            self.type_right()
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

                            ####---R RESUMO MOVTO CONTAS---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_financeiro", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_financeiro")
            self.click()
            if not self.find( "r_movtoContas_resumo", matching=0.97, waiting_time=10000):
                self.not_found("r_movtoContas_resumo")
            self.click()
            x=0
            while x<4:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            x=0
            while x<3:
                self.type_right()
                x=x+1
            x=0
            while x<3:
                self.type_right()
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

                            ####---R CHEQUES MOVTO CONTAS---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_financeiro", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_financeiro")
            self.click()
            if not self.find( "r_movtoContas_cheques", matching=0.97, waiting_time=10000):
                self.not_found("r_movtoContas_cheques")
            self.click()
            x=0
            while x<7:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
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

                            ####---R CENTRO CUSTOS MOVTO CONTAS---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_financeiro", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_financeiro")
            self.click()
            if not self.find( "r_movtoContas_CentroCusto", matching=0.97, waiting_time=10000):
                self.not_found("r_movtoContas_CentroCusto")
            self.click()
            x=0
            while x<3:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            if not self.find( "b_centroCustoInicial_r_FCC", matching=0.97, waiting_time=10000):
                self.not_found("b_centroCustoInicial_r_FCC")
            self.click_relative(189, 131)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_centroCustoFinal_r_FCC", matching=0.97, waiting_time=10000):
                self.not_found("b_centroCustoFinal_r_FCC")
            self.click_relative(195, 156)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_grupoEmpresa_r_FCC", matching=0.97, waiting_time=10000):
                self.not_found("b_grupoEmpresa_r_FCC")
            self.click_relative(42, 203)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            x=0
            while x<9:
                self.tab()
                x=x+1
            self.type_right()
            self.tab()
            self.type_up()
            self.type_down()
            self.tab()
            x=0
            while x<4:
                self.type_right()
                x=x+1
            self.tab()
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

                            ####---R CONFERENCIA CHEQUES IMPRESSOS---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_financeiro", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_financeiro")
            self.click()
            if not self.find( "r_conferenciaChequesImpressos", matching=0.97, waiting_time=10000):
                self.not_found("r_conferenciaChequesImpressos")
            self.click()
            x=0
            while x<7:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            if not self.find( "b_conta_r_RchequesImpressos", matching=0.97, waiting_time=10000):
                self.not_found("b_conta_r_RchequesImpressos")
            self.click_relative(54, 124)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_fornecedor_RchequesImpressos", matching=0.97, waiting_time=10000):
                self.not_found("b_fornecedor_RchequesImpressos")
            self.click_relative(470, 126)
            self.enter()
            self.wait(1000)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "op_ordenacao_r_chequesImpressos", matching=0.97, waiting_time=10000):
                self.not_found("op_ordenacao_r_chequesImpressos")
            self.click_relative(-5, 183)
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
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()

                            ####---R CHEQUES RECEBIDOS---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_financeiro", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_financeiro")
            self.click()
            if not self.find( "r_chequesRecebidos", matching=0.97, waiting_time=10000):
                self.not_found("r_chequesRecebidos")
            self.click()
            x=0
            while x<10:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            x=0
            while x<3:
                self.type_right()
                x=x+1
            self.tab()
            self.space()
            self.space()
            self.tab()
            self.space()
            self.space()
            self.tab()
            x=0
            while x<7:
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

                            ####---R MOVIMENTO CONTA CORRENTE---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_financeiro", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_financeiro")
            self.click()
            if not self.find( "r_movimentoContaCorrente", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentoContaCorrente")
            self.click()
            x=0
            while x<2:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.type_right()
            self.type_right()
            self.tab()
            x=0
            while x<4:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            x=0
            while x<3:
                self.type_right()
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

                            ####---R MOVIMENTO FRENTE CAIXA---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_financeiro", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_financeiro")
            self.click()
            if not self.find( "r_movimentoFrenteCaixa", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentoFrenteCaixa")
            self.click()
            x=0
            while x<2:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.type_right()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.space()
            self.space()
            self.tab()
            self.space()
            self.space()
            self.tab()
            self.tab()
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

                            ####---R RESUMO FINANCEIRO MENSAL---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_financeiro", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_financeiro")
            self.click()
            if not self.find( "r_resumoFinanceiroMensal", matching=0.97, waiting_time=10000):
                self.not_found("r_resumoFinanceiroMensal")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
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

                            ####---R RAZAO CLIENTE FORNECEDOR---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_financeiro", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_financeiro")
            self.click()
            if not self.find( "r_razaoClienteFornecedor", matching=0.97, waiting_time=10000):
                self.not_found("r_razaoClienteFornecedor")
            self.click()
            x=0
            while x<2:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.type_right()
            self.type_right()
            self.tab()
            x=0
            while x<2:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.type_right()
            self.tab()
            self.backspace()
            self.type_keys_with_interval(1,'123')
            self.tab()
            x=0
            while x<18:
                self.type_down()
                x=x+1
            x=0
            while x<18:
                self.type_up()
                x=x+1
            self.tab()
            self.type_right()
            self.tab()
            self.space()
            self.space()
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

                            ####---R CLIENTE SEM MOVIMENTO NO PERIODO---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_financeiro", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_financeiro")
            self.click()
            if not self.find( "r_clientesSemMovimento", matching=0.97, waiting_time=10000):
                self.not_found("r_clientesSemMovimento")
            self.click()
            x=0
            while x<3:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.type_right()
            self.type_right()
            self.tab()
            self.type_right()
            self.tab()
            x=0
            while x<5:
                self.type_right()
                x=x+1
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            if not self.find( "b_grupoEmpresa_r_clienteSemMovto", matching=0.97, waiting_time=10000):
                self.not_found("b_grupoEmpresa_r_clienteSemMovto")
            self.click_relative(64, 188)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            self.tab()
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

                            ####---R RECEBIMENTOS FINANCEIRO FISCAL---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_financeiro", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_financeiro")
            self.click()
            if not self.find( "r_recebimentoFinanceiro", matching=0.97, waiting_time=10000):
                self.not_found("r_recebimentoFinanceiro")
            self.click()
            x=0
            while x<3:
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

                            ####---R RELATORIO DE RESUMO---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_financeiro", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_financeiro")
            self.click()
            if not self.find( "r_relatorioDeResumo", matching=0.97, waiting_time=10000):
                self.not_found("r_relatorioDeResumo")
            self.click()
            self.type_keys_with_interval(1,'123')
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

                            ####---R EXTRATO CONTAS A PAGAR E RECEBER---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_financeiro", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_financeiro")
            self.click()
            if not self.find( "r_extratoContasPagarReceber", matching=0.97, waiting_time=10000):
                self.not_found("r_extratoContasPagarReceber")
            self.click()
            x=0
            while x<3:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            x=0
            while x<6:
                self.type_right()
                x=x+1
            self.tab()
            if not self.find( "b_grupoEmpresa_r_ExtratoContasPagarReceber", matching=0.97, waiting_time=10000):
                self.not_found("b_grupoEmpresa_r_ExtratoContasPagarReceber")
            self.click_relative(65, 138)
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
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()

                            ####---R MOV ESTOQUE POR ITENS---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_mov", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_mov")
            self.click()
            if not self.find( "r_movEstoqueItens", matching=0.97, waiting_time=10000):
                self.not_found("r_movEstoqueItens")
            self.click()
            x=0
            while x<2:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.type_right()
            self.tab()
            x=0
            while x<5:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.tab()
            self.tab()
            x=0
            while x<10:
                self.space()
                self.space()
                self.tab()
                x=x+1
            x=0
            while x<4:
                self.type_right()
                x=x+1
            self.tab()
            self.type_right()
            if not self.find( "op_situacao_r_movtoItens", matching=0.97, waiting_time=10000):
                self.not_found("op_situacao_r_movtoItens")
            self.click_relative(21, 151)
            self.type_right()
            self.type_right()
            if not self.find( "op_tipo_r_movtoItens", matching=0.97, waiting_time=10000):
                self.not_found("op_tipo_r_movtoItens")
            self.click_relative(19, 198)
            self.type_right()
            self.type_right()
            if not self.find( "op_filtroCFOP_r_movtoItens", matching=0.97, waiting_time=10000):
                self.not_found("op_filtroCFOP_r_movtoItens")
            self.click_relative(19, 254)
            self.type_right()
            self.type_right()
            if not self.find( "op_quantidades_r_movtoItens", matching=0.97, waiting_time=10000):
                self.not_found("op_quantidades_r_movtoItens")
            self.click_relative(1128, 159)
            self.type_right()
            self.type_right()
            if not self.find( "op_quantidadeUN_r_movtoItens", matching=0.97, waiting_time=10000):
                self.not_found("op_quantidadeUN_r_movtoItens")
            self.click_relative(223, 158)
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

                            ####---R MOVIMENTACAO ESTOQUE IMP GRAFICA---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_mov", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_mov")
            self.click()
            if not self.find( "r_estoqueItens_impGrafica", matching=0.97, waiting_time=10000):
                self.not_found("r_estoqueItens_impGrafica")
            self.click()
            x=0
            while x<2:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.type_right()
            self.tab()
            self.space()
            self.space()
            x=0
            while x<3:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            if not self.find( "b_grupoEmpresa_r_movtoItensIMP", matching=0.97, waiting_time=10000):
                self.not_found("b_grupoEmpresa_r_movtoItensIMP")
            self.click_relative(64, 185)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            self.tab()
            self.tab()
            x=0
            while x<7:
                self.type_right()
                x=x+1
            self.tab()
            x=0
            while x<3:
                self.type_right()
                self.type_right()
                self.tab()
                x=x+1
            self.tab()
            x=0
            while x<4:
                self.type_right()
                self.type_right()
                self.type_right()
                self.tab()
                x=x+1
            x=0
            while x<9:
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

                            ####---R ESTOQUE POR LOTES---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_mov", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_mov")
            self.click()
            if not self.find( "r_movtoEstoqueLotes", matching=0.97, waiting_time=10000):
                self.not_found("r_movtoEstoqueLotes")
            self.click()
            x=0
            while x<2:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
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

                            ####---R ESTOQUE ITENS FORNECEDORES---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_mov", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_mov")
            self.click()
            if not self.find( "r_estoqueItensFornecedor", matching=0.97, waiting_time=10000):
                self.not_found("r_estoqueItensFornecedor")
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
            x=0
            while x<7:
                self.type_right()
                x=x+1
            self.tab()
            self.tab()
            x=0
            while x<3:
                self.type_right()
                self.type_right()
                self.type_right()
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

                            ####---R MOVIMENTOS SERVICOS---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_mov", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_mov")
            self.click()
            if not self.find( "r_movimentosServicos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentosServicos")
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
            x=0
            while x<4:
                self.type_right()
                self.type_right()
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

                            ####---R MOVTO ITENS IMPOSTOS---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_mov", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_mov")
            self.click()
            if not self.find( "r_movimentoItens_impostos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentoItens_impostos")
            self.click()
            x=0
            while x<2:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.type_right()
            self.tab()
            self.tab()
            x=0
            while x<2:
                self.type_right()
                self.type_right()
                self.type_right()
                self.type_right()
                self.tab()
                x=x+1
            if not self.find( "op_filtroCFOP_r_movtoImpostos", matching=0.97, waiting_time=10000):
                self.not_found("op_filtroCFOP_r_movtoImpostos")
            self.click_relative(15, 188)
            self.type_right()
            if not self.find( "op_resumoGF_r_movtoImpostos", matching=0.97, waiting_time=10000):
                self.not_found("op_resumoGF_r_movtoImpostos")
            self.click_relative(217, 187)
            self.type_right()
            if not self.find( "op_resumoNCM_r_movtoImpostos", matching=0.97, waiting_time=10000):
                self.not_found("op_resumoNCM_r_movtoImpostos")
            self.click_relative(348, 188)
            self.type_right()
            if not self.find( "op_codBenef_r_movtoImpostos", matching=0.97, waiting_time=10000):
                self.not_found("op_codBenef_r_movtoImpostos")
            self.click_relative(460, 189)
            self.type_right()
            if not self.find( "op_itensCST_r_movtoImpostos", matching=0.97, waiting_time=10000):
                self.not_found("op_itensCST_r_movtoImpostos")
            self.click_relative(590, 188)
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

                            ####---R MOVTO ITENS CLIENTE FORNECEDOR---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_mov", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_mov")
            self.click()
            if not self.find( "r_movtoItensClienteFornecedor", matching=0.97, waiting_time=10000):
                self.not_found("r_movtoItensClienteFornecedor")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_down()
            self.type_down()
            self.type_down()
            self.tab()
            self.type_keys_with_interval(1,'123')
            if not self.find( "b_grupoEmpresa_r_ItensClienteFornecedor", matching=0.97, waiting_time=10000):
                self.not_found("b_grupoEmpresa_r_ItensClienteFornecedor")
            self.click_relative(123, 206)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            self.tab()
            self.tab()
            x=0
            while x<3:
                self.type_down()
                self.type_down()
                self.tab()
                x=x+1
            x=0
            while x<11:
                self.type_up()
                x=x+1
            self.tab()
            x=0
            while x<6:
                self.space()
                self.space()
                self.tab()
                x=x+1
            x=0
            while x<3:
                self.type_down()
                self.type_down()
                self.tab()
                x=x+1
            x=0
            while x<2:
                self.type_up()
                self.type_up()
                self.tab()
                x=x+1
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornar_filtragem", matching=0.97, waiting_time=10000):
                self.not_found("retornar_filtragem")
            self.click_relative(35, 43)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()

                            ####---R MOVTO ITENS CENTRO CUSTO---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_mov", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_mov")
            self.click()
            if not self.find( "r_movtoItensCentroCusto", matching=0.97, waiting_time=10000):
                self.not_found("r_movtoItensCentroCusto")
            self.click()
            x=0
            while x<2:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.type_right()
            self.tab()
            x=0
            while x<3:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.type_right()
            self.tab()
            self.type_right()
            self.tab()
            x=0
            while x<3:
                self.space()
                self.space()
                self.tab()
                x=x+1
            self.type_right()
            self.tab()
            self.type_right()
            self.type_right()
            x=0
            while x<8:
                self.tab()
                x=x+1
            x=0
            while x<8:
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

                            ####---R MOVTO ITENS VENDEDORES---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_mov", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_mov")
            self.click()
            if not self.find( "r_movtoItensVendedores", matching=0.97, waiting_time=10000):
                self.not_found("r_movtoItensVendedores")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
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

                            ####---R MOVTO ITENS CONTROLADOS---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_mov", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_mov")
            self.click()
            if not self.find( "r_movtoItensControlados", matching=0.97, waiting_time=10000):
                self.not_found("r_movtoItensControlados")
            self.click()
            x=0
            while x<6:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.tab()
            self.tab()
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

                            ####---R MOVTO ITENS PDV---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_mov", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_mov")
            self.click()
            if not self.find( "r_movtoItensPDV", matching=0.97, waiting_time=10000):
                self.not_found("r_movtoItensPDV")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_right()
            self.tab()
            self.type_right()
            self.type_right()
            self.type_right()
            self.tab()
            self.type_keys_with_interval(1,'123')
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

                            ####---R MOVTO ITENS PLANO PRECO---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_mov", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_mov")
            self.click()
            if not self.find( "r_movtoItensPlanoPreco", matching=0.97, waiting_time=10000):
                self.not_found("r_movtoItensPlanoPreco")
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

                            ####---MOVTO ITENS PRECO MEDIO---####
                
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_mov", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_mov")
            self.click()
            if not self.find( "r_movtoItensPrecoMedio", matching=0.97, waiting_time=10000):
                self.not_found("r_movtoItensPrecoMedio")
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
            self.type_right()
            self.tab()
            self.type_right()
            self.tab()
            self.space()
            self.space()
            self.tab()
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

                            ####---R MOVTO ITENS PRECO PRATICADO---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_mov", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_mov")
            self.click()
            if not self.find( "r_movtoItensPrecoPraticado", matching=0.97, waiting_time=10000):
                self.not_found("r_movtoItensPrecoPraticado")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            if not self.find( "b_grupoEmpresa_r_itensPraticado", matching=0.97, waiting_time=10000):
                self.not_found("b_grupoEmpresa_r_itensPraticado")
            self.click_relative(64, 200)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            self.tab()
            self.tab()
            x=0
            while x<5:
                self.type_right()
                self.type_right()
                self.type_right()
                self.tab()
                x=x+1
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

                            ####---R ITENS NAO MOVIMENTADOS PERIODO---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_mov", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_mov")
            self.click()
            if not self.find( "r_itensNaoMovtoPeriodo", matching=0.97, waiting_time=10000):
                self.not_found("r_itensNaoMovtoPeriodo")
            self.click()
            x=0
            while x<3:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            if not self.find( "b_grupoEmpresa_r_ItensSemMovimento", matching=0.97, waiting_time=10000):
                self.not_found("b_grupoEmpresa_r_ItensSemMovimento")
            self.click_relative(431, 198)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            self.tab()
            self.tab()
            x=0
            while x<6:
                self.type_right()
                x=x+1
            self.tab()
            x=0
            while x<3:
                y=0
                while y<2:
                    self.type_right()
                    y=y+1
                self.tab()
                x=x+1
            x=0
            while x<3:
                self.type_right()
                x=x+1
            self.tab()
            self.type_right()
            self.tab()
            x=0
            while x<4:
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

                            ####---R ITENS NAO MOVIMENTADOS 30 DIAS---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_mov", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_mov")
            self.click()
            if not self.find( "r_itensNaoMovtoTrinta", matching=0.97, waiting_time=10000):
                self.not_found("r_itensNaoMovtoTrinta")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            x=0
            while x<4:
                self.type_right()
                self.type_right()
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

                            ####---R CONSUMO MOVTO ANALISE---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_mov", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_mov")
            self.click()
            if not self.find( "r_consumoMovtoItens", matching=0.97, waiting_time=10000):
                self.not_found("r_consumoMovtoItens")
            self.click()
            self.type_right()
            self.tab()
            x=0
            while x<8:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            if not self.find( "b_grupoEmpresa_r_consumoMovtoAnalise", matching=0.97, waiting_time=10000):
                self.not_found("b_grupoEmpresa_r_consumoMovtoAnalise")
            self.click_relative(62, 131)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            self.tab()
            self.tab()
            self.type_right()
            self.tab()
            self.type_right()
            self.type_right()
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
            self.tab()
            self.type_right()
            self.tab()
            self.type_right()
            self.tab()
            self.type_right()
            self.tab()
            x=0
            while x<8:
                self.type_right()
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

                            ####---R ENTRADA DE DOCUMENTOS---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_mov", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_mov")
            self.click()
            if not self.find( "r_entradaPorDoc", matching=0.97, waiting_time=10000):
                self.not_found("r_entradaPorDoc")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_left()
            self.tab()
            x=0
            while x<3:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.tab()
            self.tab()
            self.type_right()
            self.tab()
            x=0
            while x<3:
                self.space()
                self.space()
                self.tab()
                x=x+1
            x=0
            while x<4:
                self.type_right()
                x=x+1
            self.tab()
            if not self.find( "op_situacao_r_entradaDoc", matching=0.97, waiting_time=10000):
                self.not_found("op_situacao_r_entradaDoc")
            self.click_relative(20, 151)
            self.type_right()
            self.type_right()
            if not self.find( "op_imprimir_r_entradaDoc", matching=0.97, waiting_time=10000):
                self.not_found("op_imprimir_r_entradaDoc")
            self.click_relative(303, 152)
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

                            ####---R ROMANEIO DE SAIDA---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_mov", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_mov")
            self.click()
            if not self.find( "r_romaneioSaida", matching=0.97, waiting_time=10000):
                self.not_found("r_romaneioSaida")
            self.click()
            self.type_keys_with_interval(1,'123')
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

                            ####---R MOVIMENTO TOTAL DOC---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_mov", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_mov")
            self.click()
            if not self.find( "r_movtoTotalDoc", matching=0.97, waiting_time=10000):
                self.not_found("r_movtoTotalDoc")
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
            x=0
            while x<5:
                self.space()
                self.space()
                self.tab()
                x=x+1
            x=0
            while x<5:
                self.type_right()
                x=x+1
            self.tab()
            self.type_right()
            self.type_right()
            self.tab()
            if not self.find( "op_siutacao_r_totalDoc", matching=0.97, waiting_time=10000):
                self.not_found("op_siutacao_r_totalDoc")
            self.click_relative(18, 154)
            self.type_right()
            self.type_right()
            if not self.find( "op_tipo_r_totalDoc", matching=0.97, waiting_time=10000):
                self.not_found("op_tipo_r_totalDoc")
            self.click_relative(290, 153)
            self.type_right()
            self.type_right()
            if not self.find( "op_imprimeDoc_r_totalDoc", matching=0.97, waiting_time=10000):
                self.not_found("op_imprimeDoc_r_totalDoc")
            self.click_relative(489, 151)
            self.type_right()
            if not self.find( "op_imprimir_r_totalDoc", matching=0.97, waiting_time=10000):
                self.not_found("op_imprimir_r_totalDoc")
            self.click_relative(633, 152)
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

                            ####---R DEMONSTRATIVO FRETE---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_mov", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_mov")
            self.click()
            if not self.find( "r_demonstrativoFretes", matching=0.97, waiting_time=10000):
                self.not_found("r_demonstrativoFretes")
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

                            ####---R MOVTO VALOR E FRETE---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_mov", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_mov")
            self.click()
            if not self.find( "r_movtoValorEFrete", matching=0.97, waiting_time=10000):
                self.not_found("r_movtoValorEFrete")
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
            while x<3:
                self.type_right()
                self.type_right()
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

                            ####---R MOVTO TOTAL VENDEDORES---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_mov", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_mov")
            self.click()
            if not self.find( "r_movtoTotalVendedores", matching=0.97, waiting_time=10000):
                self.not_found("r_movtoTotalVendedores")
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
            while x<3:
                self.type_right()
                self.type_right()
                self.tab()
                x=x+1
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

                            ####---R MOVTO ITENS FCI---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_mov", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_mov")
            self.click()
            if not self.find( "r_movtoItensFCI", matching=0.97, waiting_time=10000):
                self.not_found("r_movtoItensFCI")
            self.click()
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
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()

                            ####---R TRANSFORMACAO ITENS---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_mov", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_mov")
            self.click()
            if not self.find( "r_transItens", matching=0.97, waiting_time=10000):
                self.not_found("r_transItens")
            self.click()
            x=0
            while x<3:
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

                            ####---R ACOMPANHAMENTO DIARIO---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_mov", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_mov")
            self.click()
            if not self.find( "r_acompanhamentoDiario", matching=0.97, waiting_time=10000):
                self.not_found("r_acompanhamentoDiario")
            self.click()
            x=0
            while x<3:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.type_right()
            self.tab()
            x=0
            while x<3:
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

                            ####---R MOVIMENTACAO E SALDO ITENS---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_mov", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_mov")
            self.click()
            if not self.find( "r_movtoSaldoItens", matching=0.97, waiting_time=10000):
                self.not_found("r_movtoSaldoItens")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
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
            if not self.find( "b_grupoEmpresa_r_saldoItensFaturar", matching=0.97, waiting_time=10000):
                self.not_found("b_grupoEmpresa_r_saldoItensFaturar")
            self.click_relative(234, 127)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            self.tab()
            self.tab()
            self.type_right()
            self.tab()
            self.type_right()
            self.type_right()
            self.type_right()
            self.tab()
            self.space()
            self.space()
            self.tab()
            self.space()
            self.space()
            self.tab()
            self.tab()
            self.space()
            x=0
            while x<31:
                self.space()
                self.type_down()
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

                            ####---R MOVTO ITENS CONTROLE---####
            """
            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_mov", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_mov")
            self.click()
            if not self.find( "r_movtoItensControle", matching=0.97, waiting_time=10000):
                self.not_found("r_movtoItensControle")
            self.click()
            self.type_keys_with_interval(1,'123')
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
            if not self.find( "op_imprimir_r_movtoItensControle", matching=0.97, waiting_time=10000):
                self.not_found("op_imprimir_r_movtoItensControle")
            self.click_relative(116, 133)
            self.type_right()
            if not self.find( "op_relacionarNF_r_movtoItensControle", matching=0.97, waiting_time=10000):
                self.not_found("op_relacionarNF_r_movtoItensControle")
            self.click_relative(229, 131)
            self.type_right()
            self.type_right()
            if not self.find( "op_situacaoNF_r_movtoItensControle", matching=0.97, waiting_time=10000):
                self.not_found("op_situacaoNF_r_movtoItensControle")
            self.click_relative(527, 126)
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
            """
                            ####---R ITENS DATA VALIDADE---####

            if not self.find( "relatorios", matching=0.97, waiting_time=10000):
                self.not_found("relatorios")
            self.click()
            if not self.find( "r_movimentos", matching=0.97, waiting_time=10000):
                self.not_found("r_movimentos")
            self.click()
            if not self.find( "r_mov_itens", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens")
            self.click()
            if not self.find( "r_mov_itens_mov", matching=0.97, waiting_time=10000):
                self.not_found("r_mov_itens_mov")
            self.click()
            if not self.find( "r_itensDataValidade", matching=0.97, waiting_time=10000):
                self.not_found("r_itensDataValidade")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_down()
            self.type_down()
            self.tab()
            self.type_right()
            self.type_right()
            self.type_right()
            self.type_right()
            self.tab()
            self.type_right()
            self.tab()
            self.type_right()
            self.type_right()
            self.type_right()
            self.tab()
            if not self.find( "b_grupoEmpresa_r_itensDataValidade", matching=0.97, waiting_time=10000):
                self.not_found("b_grupoEmpresa_r_itensDataValidade")
            self.click_relative(65, 192)
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
            self.type_right()
            self.type_right()
            self.type_right()
            self.type_right()
            self.type_right()
            self.tab()
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

























































































































































































































