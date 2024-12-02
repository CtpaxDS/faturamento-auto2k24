        
from botcity.core import DesktopBot

class Bot(DesktopBot):
        def action(self, execution=None):

            #######################-----LOGIN-----############################

            self.execute(r"C:\teorema\bin\transportes.exe")
        
            if not self.find( "btn_codigo_usuario", matching=0.97, waiting_time=100000):
                self.not_found("btn_codigo_usuario")
            self.click_relative(47, 12)
                    
            self.type_keys_with_interval(1,"999")
            self.type_keys_with_interval(1,"tsfmx24")
            self.enter()

            if not self.find( "btn_login", matching=0.97, waiting_time=10000):
                self.not_found("btn_login")
            self.click()
            self.enter()
            self.wait(1000)
            self.enter()
         
            ###################################################################
            self.wait(1000)
            if not self.find( "transportes_cadastros1", matching=0.97, waiting_time=10000):
                self.not_found("transportes_cadastros1")
            self.click()
            self.wait(500)
            if not self.find( "transportes_empresas2", matching=0.97, waiting_time=10000):
                self.not_found("transportes_empresas2")
            self.click()
            self.wait(500)
            if not self.find( "transportes_empresas2", matching=0.97, waiting_time=10000):
                self.not_found("transportes_empresas2")
            self.click()
            if not self.find( "transporte_localizarempresa", matching=0.97, waiting_time=10000):
                self.not_found("transporte_localizarempresa")
            self.click_relative(100, 50)
            if not self.find( "transporte_incluir_001", matching=0.97, waiting_time=10000):
                self.not_found("transporte_incluir_001")
            self.click_relative(150, 48)
            if not self.find( "transportes_nao", matching=0.97, waiting_time=10000):
                self.not_found("transportes_nao")
            self.click()
            x=0
            while x<3:
                if not self.find( "indentificador", matching=0.97, waiting_time=10000):
                    self.not_found("indentificador")
                self.click_relative(110, 25)
                self.type_down()
                self.enter()
                x=x+1    
            self.type_keys_with_interval(1,"jm12$%")
            self.tab()
            self.type_keys_with_interval(1,"14736820969")
            self.tab()
            self.type_keys_with_interval(1,"9999999999999999")
            self.tab()
            self.type_down()
            self.type_up()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,"jm123#$")
            x=0
            while x<5:
                if not self.find( "transportes_cadastro4", matching=0.97, waiting_time=10000):
                    self.not_found("transportes_cadastro4")
                self.click_relative(558, 195)
                self.type_down()
                self.enter()
                x=x+1
            self.tab()
            x=0
            while x<8:
                if not self.find( "transporte_cadastroempresa5", matching=0.97, waiting_time=10000):
                        self.not_found("transporte_cadastroempresa5")
                self.click_relative(676, 194)
                self.type_down()
                self.enter()
                x=x+1
            self.type_keys_with_interval(1,"72141517")
            self.tab()
            self.type_keys_with_interval(1,"72141517")
            self.tab()
            self.type_keys_with_interval(1,"72141517")
            self.tab()
            self.type_keys_with_interval(1,"203040")
            self.tab()
            self.type_keys_with_interval(1,"152790")
            self.tab()
            self.type_keys_with_interval(1,"152709")
            self.tab()
            self.type_keys_with_interval(1,"vereador alvares nascimento")
            self.tab()
            self.type_keys_with_interval(1,"181")
            self.tab()
            if not self.find( "transporte_cadastrodeempresa6", matching=0.97, waiting_time=10000):
                self.not_found("transporte_cadastrodeempresa6")
            self.click_relative(702, 297)
            if not self.find( "transporte_consultaminicip", matching=0.97, waiting_time=10000):
                self.not_found("transporte_consultaminicip")
            self.click_relative(19, 95)
            if not self.find( "selecionar_muncipios_cadastro", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_muncipios_cadastro")
            self.click()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,"152718")
            self.tab()
            self.type_keys_with_interval(1,"apartamento")
            self.tab()
            self.type_keys_with_interval(1,"santana")
            self.tab()
            self.type_keys_with_interval(1,"42999478085")
            self.tab()
            self.type_keys_with_interval(1,"15361458")
            self.tab()
            self.type_keys_with_interval(1,"teste@testeteorema.com.br")
            self.tab()
            #if not self.find( "transporte_cadastrodeempresa08", matching=0.97, waiting_time=10000):
                  #self.not_found("transporte_cadastrodeempresa08")
            #self.click_relative(442, 399)
            #if not self.find( "transporte_adicionar_conta", matching=0.97, waiting_time=10000):
                #self.not_found("transporte_adicionar_conta")
            #self.click()
            #if not self.find( "fechar_email_transporte", matching=0.97, waiting_time=10000):
                #self.not_found("fechar_email_transporte")
            #self.click_relative(427, 10)
            #if not self.find( "transporte_fechar_transporte", matching=0.97, waiting_time=10000):
                #self.not_found("transporte_fechar_transporte")
            #self.click()
            #self.tab()
            self.type_keys_with_interval(1,"www.google.com")
            if not self.find( "abrir_navegador", matching=0.97, waiting_time=10000):
                self.not_found("abrir_navegador")
            self.click()    
            if not self.find( "fechar_google_transporte", matching=0.97, waiting_time=10000):
                self.not_found("fechar_google_transporte")
            self.click_relative(220, 9)
            self.tab()
            self.type_keys_with_interval(1,"joao mateus")
            if not self.find( "transportes_b_funcaoresponsavel", matching=0.97, waiting_time=10000):
                self.not_found("transportes_b_funcaoresponsavel")
            self.click_relative(52, 30)
            if not self.find( "transporte_consultadefunc02", matching=0.97, waiting_time=10000):
                self.not_found("transporte_consultadefunc02")
            self.click_relative(82, 92)      
            if not self.find( "selecionar_funcoes", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_funcoes")
            self.click()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,"fernando de lima")
            self.tab()
            self.type_keys_with_interval(1,"empresario")
            self.tab()
            self.type_keys_with_interval(1,"14736820969")
            self.tab()
            self.type_keys_with_interval(1,"eduardo lima")
            self.tab()
            self.type_keys_with_interval(1,"20253035")
            self.tab()
            self.type_keys_with_interval(1,"245")
            self.tab()
            self.type_keys_with_interval(1,"contador")
            self.tab()
            self.type_keys_with_interval(1,"luisfernando@gmail.com")
            self.tab()
            self.type_keys_with_interval(1,"4299478085")
            self.tab()
            self.type_keys_with_interval(1,"365")
            self.tab()
            self.type_keys_with_interval(1,"2515")
            self.tab()
            self.type_keys_with_interval(1,"1202")
            self.tab()
            self.type_keys_with_interval(1,"1301")
            self.tab()
            self.type_keys_with_interval(1,"2502")
            #if not self.find( "transporte_cadastroempresa10", matching=0.97, waiting_time=10000):
                #self.not_found("transporte_cadastroempresa10")
            #self.click_relative(152, 129)
            #if not self.find( "transporte_arrendodamento", matching=0.97, waiting_time=10000):
            #    self.not_found("transporte_arrendodamento")
            #self.click()q
            if not self.find( "transporte_info_02", matching=0.97, waiting_time=10000):
                self.not_found("transporte_info_02")
            self.click_relative(192, 137)
            self.type_keys_with_interval(1,"123456")
            self.tab()
            self.type_keys_with_interval(1,"123748")
            self.tab()
            self.type_keys_with_interval(1,"1234")
            self.tab()
            self.type_keys_with_interval(1,"123")
            self.tab()
            self.type_keys_with_interval(1,"123456")
            self.tab()
            self.type_keys_with_interval(1,"123456")
            self.tab()
            self.type_keys_with_interval(1,"123456")
            self.tab()
            self.type_keys_with_interval(1,"123456")
            self.tab()
            self.type_keys_with_interval(1,"123456")
            self.tab()
            self.type_keys_with_interval(1,"123456")
            self.tab()
            self.type_keys_with_interval(1,"123123")
            self.tab()
            self.type_keys_with_interval(1,"20")
            self.tab()
            self.type_keys_with_interval(1,"12134")
            x=0
            while x<5:
                if not self.find( "transporte_cadastrodeempresa11", matching=0.97, waiting_time=10000):
                   self.not_found("transporte_cadastrodeempresa11")
                self.click_relative(456, 264)
                self.type_down()
                self.enter()
                x=x+1
            self.tab()
            x=0
            while x<4:
                 if not self.find( "transporte_cadastrodeempresa12", matching=0.97, waiting_time=10000):
                     self.not_found("transporte_cadastrodeempresa12")
                 self.click_relative(717, 263)
                 self.type_down()
                 self.enter()
                 x=x+1
            self.tab()
            x=0
            while x<4:
                if not self.find( "transporte_indicacao_02", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_indicacao_02")
                self.click_relative(978, 269)
                self.type_down()
                self.enter()
                x=x+1
            self.type_keys_with_interval(1,"123456789")
            self.tab()
            self.type_keys_with_interval(1,"1545")
            self.tab()
            self.type_keys_with_interval(1,"152345")
            self.tab()
            self.type_keys_with_interval(1,"25214")
            self.tab()
            self.type_keys_with_interval(1,"143025")
            self.tab()
            x=0
            while x<6:
                if not self.find( "transporte_cadastrodeempresa14", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_cadastrodeempresa14")
                self.click_relative(870, 328)
                self.type_up()
                self.enter()
                x=x+1
            self.type_keys_with_interval(1,"Rio grande do sul")
            self.tab()
            self.type_keys_with_interval(1,"257236")
            self.tab()
            self.type_keys_with_interval(1,"09022003")
            self.tab()
            self.type_keys_with_interval(1,"11112011")
            self.tab()
            self.type_keys_with_interval(1,"12122012")
            self.tab()
            self.type_keys_with_interval(1,"130920003")
            self.tab()
            self.type_keys_with_interval(1,"210920003")
            self.tab()
            self.type_keys_with_interval(1,"4520")
            ############################################################]
            #rais/dsr/gps/sefip/caged
            if not self.find( "transporte_informacao01", matching=0.97, waiting_time=10000):
                self.not_found("transporte_informacao01")
            self.click_relative(186, 37)
            if not self.find( "transporte_clickconfirm", matching=0.97, waiting_time=10000):
                   self.not_found("transporte_clickconfirm")
            self.click_relative(88, 208)
            if not self.find( "transporte_cadastrodeempresa15", matching=0.97, waiting_time=10000):
                self.not_found("transporte_cadastrodeempresa15")
            self.click_relative(215, 208)
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.type_keys_with_interval(1,"2020")
            self.tab()
            x=0
            while x<3:
                if not self.find( "transporte_enquandramento", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_enquandramento")
                self.click_relative(596, 221)
                self.type_down()
                self.enter()
                x=x+1
            self.type_keys_with_interval(1,"12112003")
            self.tab()
            self.type_keys_with_interval(1,"10")
            self.tab()
            self.type_keys_with_interval(1,"10")
            self.tab()
            self.type_keys_with_interval(1,"1520")
            self.tab()
            self.type_keys_with_interval(1,"202030")
            self.tab()
            self.type_keys_with_interval(1,"202020")
            self.tab()
            self.type_keys_with_interval(1,"202020")
            self.tab()
            self.type_keys_with_interval(1,"303030")
            self.tab()
            self.type_keys_with_interval(1,"404040")
            self.tab()
            self.type_keys_with_interval(1,"50505050")
            self.tab()
            self.type_keys_with_interval(1,"606060")
            self.tab()
            self.type_keys_with_interval(1,"707070")
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.space()
            x=0
            while x<7:
                if not self.find( "transporte_controledeponto", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_controledeponto")
                self.click_relative(738, 464)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<2:
                if not self.find( "transporte_cadastrodeempresa24", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_cadastrodeempresa24")
                self.click_relative(740, 505)
                self.type_down()
                self.enter()
                x=x+1
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.space()
            x=0
            while x<3:
                if not self.find( "transporte_alterarCNAE", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_alterarCNAE")
                self.click_relative(496, 343)
                self.type_down()
                self.enter()
                x=x+1
            self.type_keys_with_interval(1,"203")
            self.tab()
            x=0
            while x<3:
                if not self.find( "tipo_centralizacao", matching=0.97, waiting_time=10000):
                    self.not_found("tipo_centralizacao")
                self.click_relative(108, 25)
                self.type_down()
                x=x+1
            ################################################################################################################
                                                       #CAGED
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.type_keys_with_interval(1,"2525")
            self.tab()
            x=0
            while x<3:
                if not self.find( "transporte_informacao", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_informacao")
                self.click_relative(109, 30)
                self.type_down()
                self.enter()
                x=x+1
            #gps_
            if not self.find( "codigo_gps", matching=0.97, waiting_time=10000):
                self.not_found("codigo_gps")
            self.click_relative(54, 35)
            self.type_keys_with_interval(1,"775")
            self.enter()
            self.type_keys_with_interval(1,"333")
            self.enter()
            self.type_keys_with_interval(1,"333")
            self.enter()
            self.type_keys_with_interval(1,"333")
            self.enter()
            self.type_keys_with_interval(1,"333")
            self.enter()
            self.type_keys_with_interval(1,"333")
            self.enter()
            self.type_keys_with_interval(1,"333")
            self.enter()
            self.type_keys_with_interval(1,"3333")
            self.enter()
            self.type_keys_with_interval(1,"333")
            self.enter()
            self.type_keys_with_interval(1,"333")
            self.enter()
            self.type_keys_with_interval(1,"333")
            self.enter()
            self.type_keys_with_interval(1,"333")
            self.enter()
            self.space()

            ########################################################################################################################################
                                           #mensagens e observações    
            if not self.find( "mensagens_observacoes", matching=0.97, waiting_time=10000):
                self.not_found("mensagens_observacoes")
            self.click()
            self.type_keys_with_interval(1,"adasdsa1515")
            self.tab()
            self.type_keys_with_interval(1,"dadsaeqrfe3535")
            self.tab()
            self.type_keys_with_interval(1,"deqreqr666")
            #######################################################################################################################################
                                        #Informações fiscais
            if not self.find( "transporte_infofiscais", matching=0.97, waiting_time=10000):
                 self.not_found("transporte_infofiscais")
            self.click_relative(334, 136)
            self.type_keys_with_interval(1,"254569")
            self.tab()
            self.type_keys_with_interval(1,"25112010")
            self.tab()
            self.type_keys_with_interval(1,"5050")
            self.tab()
            self.type_keys_with_interval(1,"7575")
            x=0
            while x<7:
                if not self.find( "transporte_simples_001", matching=0.97, waiting_time=10000):
                   self.not_found("transporte_simples_001")
                self.click_relative(465, 29)
                self.type_up()
                self.enter()
                x=x+1
            self.tab()
            x=0
            while x<8:
                if not self.find( "transporte_faixasimples", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_faixasimples")
                self.click_relative(1250, 260)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<4:
                if not self.find( "transporte_naturezajuridica", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_naturezajuridica")
                self.click_relative(300, 319)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<7:
                if not self.find( "transporte_tipodeatividade", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_tipodeatividade")
                self.click_relative(615, 318)
                self.type_down()
                self.enter()
                x=x+1
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.type_keys_with_interval(1,"12")
            self.tab()
            self.type_keys_with_interval(1,"12526")
            x=0
            while x<3:
                if not self.find( "transporte_tipodedeclarente", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_tipodedeclarente")
                self.click_relative(676, 442)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<7:
                if not self.find( "transporte_class", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_class")
                self.click_relative(470, 500)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<8:
                if not self.find( "transporte_locatributaria", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_locatributaria")
                self.click_relative(951, 501)
                self.type_down()
                self.enter()
                x=x+1
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.space()
            x=0
            while x<4:
                if not self.find( "transporte_cooperativa", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_cooperativa")
                self.click_relative(991, 261)
                self.type_down()
                self.enter()
                x=x+1
          ##########################################################################################################################################
                #Agrupamentos   
            if not self.find( "transporte_agrupamentos", matching=0.97, waiting_time=10000):
                self.not_found("transporte_agrupamentos")
            self.click_relative(405, 134)
            if not self.find( "transporte_grupo_de_empresa", matching=0.97, waiting_time=10000):
                self.not_found("transporte_grupo_de_empresa")
            self.click_relative(62, 32)
            self.type_keys_with_interval(1,"001")
            if not self.find( "transporte_consulta_grupo_de_empresa", matching=0.97, waiting_time=10000):
                self.not_found("transporte_consulta_grupo_de_empresa")
            self.click_relative(150, 48)
            if not self.find( "transporte_clientes_fornecedores", matching=0.97, waiting_time=10000):
                self.not_found("transporte_clientes_fornecedores")
            self.click_relative(26, 247)
###############################################################
            if not self.find( "transporte_cadastroclientes", matching=0.97, waiting_time=10000):
                self.not_found("transporte_cadastroclientes")
            self.click_relative(79, 237)
            self.type_keys_with_interval(1,"0001")
            if not self.find( "transporte_localizarcliente", matching=0.97, waiting_time=10000):
                self.not_found("transporte_localizarcliente")
            self.click_relative(164, 39)
            if not self.find( "cadastro_planodecustos", matching=0.97, waiting_time=10000):
                self.not_found("cadastro_planodecustos")
            self.click_relative(75, 288)
            self.type_keys_with_interval(1,"0001")
            if not self.find( "transporte_planodescusto02", matching=0.97, waiting_time=10000):
                self.not_found("transporte_planodescusto02")
            self.click_relative(159, 43)

            #if not self.find( "transporte_tabeladeprecos", matching=0.97, waiting_time=10000):
                #self.not_found("transporte_tabeladeprecos")
            #self.click_relative(78, 335)
            #self.type_keys_with_interval(1,"0001")
#######################################

            if not self.find( "transporte_contatosdaempresa", matching=0.97, waiting_time=10000):
                self.not_found("transporte_contatosdaempresa")
            self.click_relative(76, 373)
            self.type_keys_with_interval(1,"0001")
            if not self.find( "transporte_selecionar_contratos_de_empresa", matching=0.97, waiting_time=10000):
                self.not_found("transporte_selecionar_contratos_de_empresa")
            self.click()
            if not self.find( "transporte_planodecontas", matching=0.97, waiting_time=10000):
                self.not_found("transporte_planodecontas")
            self.click_relative(496, 193)
            self.type_keys_with_interval(1,"0010")
            if not self.find( "transporte_selecionar_plano_de_contas", matching=0.97, waiting_time=10000):
                self.not_found("transporte_selecionar_plano_de_contas")
            self.click()
            #if not self.find( "transporte_agroindustria", matching=0.97, waiting_time=10000):
                #self.not_found("transporte_agroindustria")
            #self.click_relative(159, 41)
            if not self.find( "transporte_itensdaempresa", matching=0.97, waiting_time=10000):
                self.not_found("transporte_itensdaempresa")
            self.click_relative(500, 248)
            self.type_keys_with_interval(1,"0010")
            if not self.find( "transporte_itens", matching=0.97, waiting_time=10000):
                self.not_found("transporte_itens")
            self.click_relative(158, 44)
            
            if not self.find( "transporte_vendedores", matching=0.97, waiting_time=10000):
                self.not_found("transporte_vendedores")
            self.click_relative(495, 283)
            self.type_keys_with_interval(1,"0001")
            if not self.find( "transporte_selecionar_vendedores_de_empresa", matching=0.97, waiting_time=10000):
                self.not_found("transporte_selecionar_vendedores_de_empresa")
            self.click()
            if not self.find( "transporte_contabilista", matching=0.97, waiting_time=10000):
                self.not_found("transporte_contabilista")
            self.click_relative(498, 373)
            if not self.find( "transporte_consultaclientes", matching=0.97, waiting_time=10000):
                self.not_found("transporte_consultaclientes")
            self.click_relative(40, 36)
            if not self.find( "transporte_precodaempresa", matching=0.97, waiting_time=10000):
                self.not_found("transporte_precodaempresa")
            self.click_relative(915, 245)
            self.type_keys_with_interval(1,"0001")
            if not self.find( "transporte_precoempresa01", matching=0.97, waiting_time=10000):
               self.not_found("transporte_precoempresa01")
            self.click_relative(167, 44)
     
            if not self.find( "transporte_cadastro_situacao_empresa", matching=0.97, waiting_time=10000):
                self.not_found("transporte_cadastro_situacao_empresa")
            self.click_relative(8, 25)
            
            
            self.type_keys_with_interval(1,"0001")
            ######################
            if not self.find( "transporte_veiculos_02", matching=0.97, waiting_time=10000):
                self.not_found("transporte_veiculos_02")
            self.click_relative(69, 33) 
            if not self.find( "transporte_localizarerror", matching=0.97, waiting_time=10000):
                self.not_found("transporte_localizarerror")
            self.click_relative(161, 43)
            if not self.find( "transporte_veiculos", matching=0.97, waiting_time=10000):
                self.not_found("transporte_veiculos")
            self.click_relative(918, 335)
            self.type_keys_with_interval(1,"0010")
            #
            #
            if not self.find( "transporte_selecionar_veiculos_empresa", matching=0.97, waiting_time=10000):
                self.not_found("transporte_selecionar_veiculos_empresa")
            self.click()
            if not self.find( "transporte_contasdecliente", matching=0.97, waiting_time=10000):
                self.not_found("transporte_contasdecliente")
            self.click()    
 ############################################################################################################################################               
            if not self.find( "transporte_contasdecliente", matching=0.97, waiting_time=10000):
                self.not_found("transporte_contasdecliente")
            self.click_relative(128, 436)
            if not self.find( "transporte_limparcampo", matching=0.97, waiting_time=10000):
                self.not_found("transporte_limparcampo")
            self.click_relative(178, 482)
            
            if not self.find( "transporte_contabil99990", matching=0.97, waiting_time=10000):
                self.not_found("transporte_contabil99990")
            self.click_relative(139, 482)
            if not self.find( "trasnporte_limparcampo02", matching=0.97, waiting_time=10000):
                self.not_found("trasnporte_limparcampo02")
            self.click_relative(204, 527)
            if not self.find( "transporte_contabil99982", matching=0.97, waiting_time=10000):
                self.not_found("transporte_contabil99982")
            self.click_relative(137, 523)
            if not self.find( "transporte_limparcampo03", matching=0.97, waiting_time=10000):
                self.not_found("transporte_limparcampo03")
            self.click_relative(191, 570)
            ################################################################################################################
            if not self.find( "transporte_fornecedores", matching=0.97, waiting_time=10000):
                self.not_found("transporte_fornecedores")
            self.click_relative(297, 433)
            if not self.find( "transporte_limparcampoerror01", matching=0.97, waiting_time=10000):
                self.not_found("transporte_limparcampoerror01")
            self.click_relative(374, 481)      
            if not self.find( "transporte_contacontabil99989", matching=0.97, waiting_time=10000):
                self.not_found("transporte_contacontabil99989")
            self.click_relative(291, 477)
            if not self.find( "transporte_limparcampo05", matching=0.97, waiting_time=10000):
                self.not_found("transporte_limparcampo05")
            self.click_relative(370, 527)
            if not self.find( "transporte_contabil99981", matching=0.97, waiting_time=10000):
                self.not_found("transporte_contabil99981")
            self.click_relative(292, 518)
            if not self.find( "transporte_limparcampo06", matching=0.97, waiting_time=10000):
                self.not_found("transporte_limparcampo06")
            self.click_relative(343, 571)
            if not self.find( "transporte_contabil99996", matching=0.97, waiting_time=10000):
                self.not_found("transporte_contabil99996")
            self.click_relative(455, 429)
            if not self.find( "transporte_limparcampo07", matching=0.97, waiting_time=10000):
                self.not_found("transporte_limparcampo07")
            self.click_relative(504, 476)
            if not self.find( "transporte_contabil99988", matching=0.97, waiting_time=10000):
                self.not_found("transporte_contabil99988")
            self.click_relative(455, 479)
            if not self.find( "transporte_limparcampo08", matching=0.97, waiting_time=10000):
                self.not_found("transporte_limparcampo08")
            self.click_relative(527, 522)
            if not self.find( "transporte_contabil99995", matching=0.97, waiting_time=10000):
                self.not_found("transporte_contabil99995")
            self.click_relative(620, 431)
            if not self.find( "transporte_limparcampo09", matching=0.97, waiting_time=10000):
                self.not_found("transporte_limparcampo09")
            self.click_relative(657, 483)
            if not self.find( "transporte_contabil99987", matching=0.97, waiting_time=10000):
                self.not_found("transporte_contabil99987")
            self.click_relative(617, 480)
            if not self.find( "trasnporte_limparcampo10", matching=0.97, waiting_time=10000):
                self.not_found("trasnporte_limparcampo10")
            self.click_relative(697, 528)
            if not self.find( "trasnporte_contabil99994", matching=0.97, waiting_time=10000):
                self.not_found("trasnporte_contabil99994")
            self.click_relative(772, 437)
            if not self.find( "trasnporte_limparcampo11", matching=0.97, waiting_time=10000):
                self.not_found("trasnporte_limparcampo11")
            self.click_relative(803, 481)
            if not self.find( "trasnporte_contabil99986", matching=0.97, waiting_time=10000):
                self.not_found("trasnporte_contabil99986")
            self.click_relative(773, 469)
            if not self.find( "transporte_limparcampo12", matching=0.97, waiting_time=10000):
                self.not_found("transporte_limparcampo12")
            self.click_relative(862, 530)
            if not self.find( "transporte_contabil99993", matching=0.97, waiting_time=10000):
                self.not_found("transporte_contabil99993")
            self.click_relative(935, 433)
            if not self.find( "transporte_campo13", matching=0.97, waiting_time=10000):
                self.not_found("transporte_campo13")
            self.click_relative(975, 482)
############################################################################################################################
            if not self.find( "transporte_contabil99985", matching=0.97, waiting_time=10000):
                self.not_found("transporte_contabil99985")
            self.click_relative(934, 477)
            if not self.find( "transporte_limparcampoerror02", matching=0.97, waiting_time=10000):
                self.not_found("transporte_limparcampoerror02")
            self.click_relative(967, 524)
            if not self.find( "transporte_contabil99992", matching=0.97, waiting_time=10000):
                self.not_found("transporte_contabil99992")
            self.click_relative(1095, 436)
            if not self.find( "transporte_limparcampo15", matching=0.97, waiting_time=10000):
                self.not_found("transporte_limparcampo15")
            self.click_relative(1140, 482)
            if not self.find( "transporte_contabil99984", matching=0.97, waiting_time=10000):
                self.not_found("transporte_contabil99984")
            self.click_relative(1096, 479)
            if not self.find( "transporte_limparcampo16", matching=0.97, waiting_time=10000):
                self.not_found("transporte_limparcampo16")
            self.click_relative(1146, 528)
            if not self.find( "transporte_contabil99991", matching=0.97, waiting_time=10000):
                self.not_found("transporte_contabil99991")
            self.click_relative(1258, 430)
            if not self.find( "transporte_limparcampo17", matching=0.97, waiting_time=10000):
                self.not_found("transporte_limparcampo17")
            self.click_relative(1147, 482)
            if not self.find( "transporte_99983", matching=0.97, waiting_time=10000):
                self.not_found("transporte_99983")
            self.click_relative(1257, 475)
            if not self.find( "transporte_limparcampo19", matching=0.97, waiting_time=10000):
                self.not_found("transporte_limparcampo19")
            self.click_relative(1122, 521)
            self.tab()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,"1231")
            ####################################################################################################################################
                                    #relacionados   
            if not self.find( "transporte_relacionados", matching=0.97, waiting_time=10000):
                self.not_found("transporte_relacionados")
            self.click_relative(508, 128)     
            if not self.find( "transporte_salvar_relacionamento", matching=0.97, waiting_time=10000):
                self.not_found("transporte_salvar_relacionamento")
            self.click()
            if not self.find( "transporte_incluir_cadas", matching=0.97, waiting_time=10000):
                 self.not_found("transporte_incluir_cadas")
            self.click_relative(20, 160)
            if not self.find( "transporte_estado", matching=0.97, waiting_time=10000):
                self.not_found("transporte_estado")
            self.click_relative(85, 218)
            self.type_keys_with_interval(1,"001")
            if not self.find( "transporte_consultadeestados", matching=0.97, waiting_time=10000):
                self.not_found("transporte_consultadeestados")
            self.click_relative(163, 42)
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,"123")
            if not self.find( "transporte_gravar", matching=0.97, waiting_time=10000):
                self.not_found("transporte_gravar")
            self.click_relative(581, 214)
            if not self.find( "transporte_cancelar00", matching=0.97, waiting_time=10000):
                self.not_found("transporte_cancelar00")
            self.click_relative(670, 220)          
            if not self.find( "transporte_confirmar_cancelar", matching=0.97, waiting_time=10000):
                self.not_found("transporte_confirmar_cancelar")
            self.click()
            if not self.find( "transporte_excluir_inscricoes_Estaduais", matching=0.97, waiting_time=10000):
                self.not_found("transporte_excluir_inscricoes_Estaduais")
            self.click()
          ###################################################################################################################
                                                 #cadastrosocios
            if not self.find( "transporte_socios", matching=0.97, waiting_time=10000):
                self.not_found("transporte_socios")
            self.click_relative(192, 160)
            if not self.find( "transporte_incluir_error", matching=0.97, waiting_time=10000):
                self.not_found("transporte_incluir_error")
            self.click_relative(17, 155)
            self.type_keys_with_interval(1,"jmrm12#$")
            self.tab()
            self.type_keys_with_interval(1,"090920003")
            self.tab()
            self.type_keys_with_interval(1,"99999999999")
            self.tab()
            self.type_keys_with_interval(1,"9999999999")
            self.tab()
            self.type_keys_with_interval(1,"1520")
            self.tab()
            self.type_keys_with_interval(1,"aaaaaaaaa")
            self.tab()
            self.type_keys_with_interval(1,"asasasasasas")
            x=0
            while x<8:
                if not self.find( "uf", matching=0.97, waiting_time=10000):
                    self.not_found("uf")
                self.click_relative(214, 28)
                self.type_down()
                self.enter()
                x=x+1
            self.type_keys_with_interval(1,"12121212")
            self.tab()
            self.type_keys_with_interval(1,"trianon")
            self.tab()
            self.type_keys_with_interval(1,"sobrado")
            self.tab()
            self.type_keys_with_interval(1,"429999999")
            self.tab()
            self.type_keys_with_interval(1,"testeteste@gmail.com")
            self.tab()
            x=0
            while x<7:
                if not self.find( "transporte_ocorrencia", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_ocorrencia")
                self.click_relative(9, 31)
                self.type_down()
                self.type_down()
                self.enter()
                x=x+1
            self.type_keys_with_interval(1,"12/03/2002")
            self.tab()
            x=0
            while x<8:
                if not self.find( "transporte_categoria", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_categoria")
                self.click_relative(892, 400)
                self.type_down()
                self.enter()
                x=x+1
            self.type_keys_with_interval(1,"12122024")
            self.tab()
            self.type_keys_with_interval(1,"12022024")
            self.tab()
            self.type_keys_with_interval(1,"12")
            self.tab()
            self.type_keys_with_interval(1,"22")
            self.tab()
            self.type_keys_with_interval(1,"90")
            self.tab()
            self.type_keys_with_interval(1,"30")
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            if not self.find( "transporte_funcao", matching=0.97, waiting_time=10000):
                self.not_found("transporte_funcao")
            self.click_relative(331, 30)
            if not self.find( "transporte_acompanhanteidoso", matching=0.97, waiting_time=10000):
                self.not_found("transporte_acompanhanteidoso")
            self.click_relative(257, 399)
            if not self.find( "transporte_banco", matching=0.97, waiting_time=10000):
                self.not_found("transporte_banco")
            self.click_relative(325, 22)
            if not self.find( "transporte_bradesco", matching=0.97, waiting_time=10000):
                self.not_found("transporte_bradesco")
            self.click_relative(631, 442)
            self.tab()
            self.type_keys_with_interval(1,"123456789")
            self.tab()
            self.type_keys_with_interval(1,"12334")
            self.tab()
            self.type_keys_with_interval(1,"asd12#$")
            if not self.find( "transporte_concluido", matching=0.97, waiting_time=10000):
                self.not_found("transporte_concluido")
            self.click_relative(16, 205)
           #######################################
            if not self.find( "transporte_cancel", matching=0.97, waiting_time=10000):
                self.not_found("transporte_cancel")
            self.click_relative(20, 224)
            if not self.find( "transporte_sim_cancelar_operacaoo_socios", matching=0.97, waiting_time=10000):
                self.not_found("transporte_sim_cancelar_operacaoo_socios")
            self.click()
            if not self.find( "transporte_excluir_socios_00", matching=0.97, waiting_time=10000):
                self.not_found("transporte_excluir_socios_00")
            self.click()
            if not self.find( "transporte_sim01", matching=0.97, waiting_time=10000):
                self.not_found("transporte_sim01")
            self.click_relative(95, 128)
  ########################################################################################################################
                            #relacionamentos documentos
            if not self.find( "transporte_documento_02", matching=0.97, waiting_time=10000):
                self.not_found("transporte_documento_02")
            self.click_relative(243, 157)
            if not self.find( "transporte_incluir", matching=0.97, waiting_time=10000):
                self.not_found("transporte_incluir")
            self.click_relative(18, 162)
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,"22052015")
            if not self.find( "transporte_calendario", matching=0.97, waiting_time=10000):
                self.not_found("transporte_calendario")
            self.click_relative(492, 216)
            if not self.find( "transporte_insidedocumento", matching=0.97, waiting_time=10000):
                self.not_found("transporte_insidedocumento")
            self.click_relative(918, 218)
            if not self.find( "fechar_doc", matching=0.97, waiting_time=10000):
                self.not_found("fechar_doc")
            self.click()
            if not self.find( "transporte_cancel", matching=0.97, waiting_time=10000):
                self.not_found("transporte_cancel")
            self.click_relative(16, 227)
            if not self.find( "transporte_confirmar_documentos", matching=0.97, waiting_time=10000):
                 self.not_found("transporte_confirmar_documentos")
            self.click()
##########################################################################################
                                    #pessoasautorizadas            
            if not self.find( "transporte_pessoas_autorizadas", matching=0.97, waiting_time=10000):
                self.not_found("transporte_pessoas_autorizadas")
            self.click_relative(337, 162)
            if not self.find( "transporte_incluir_pessoas", matching=0.97, waiting_time=10000):
                self.not_found("transporte_incluir_pessoas")
            self.click_relative(18, 158)
            if not self.find( "transporte_clientes", matching=0.97, waiting_time=10000):
                 self.not_found("transporte_clientes")
            self.click_relative(445, 228)
            if not self.find( "transporte_joelzanardini", matching=0.97, waiting_time=10000):
                 self.not_found("transporte_joelzanardini")
            self.click_relative(291, 265)
            if not self.find( "transporte_situacao", matching=0.97, waiting_time=10000):
                 self.not_found("transporte_situacao")
            self.click_relative(763, 226)
            self.tab()
            self.type_keys_with_interval(1,"asd12!@")
            if not self.find( "transporte_confirmarcadastro", matching=0.97, waiting_time=10000):
                self.not_found("transporte_confirmarcadastro")
            self.click_relative(18, 209)
            if not self.find( "transporte_cancelcadastro", matching=0.97, waiting_time=10000):
                self.not_found("transporte_cancelcadastro")
            self.click_relative(18, 226)
            if not self.find( "transporte_confirmarcancel", matching=0.97, waiting_time=10000):
                self.not_found("transporte_confirmarcancel")
            self.click_relative(107, 121)
            if not self.find( "transporte_excluircadastro", matching=0.97, waiting_time=10000):
                self.not_found("transporte_excluircadastro")
            self.click_relative(18, 183)
            if not self.find( "transporte_confirmarexlcuir", matching=0.97, waiting_time=10000):
                self.not_found("transporte_confirmarexlcuir")
            self.click_relative(90, 125)
######################################################################################################################################################
                        #GNRE
            if not self.find( "transporte_gnre", matching=0.97, waiting_time=10000):
                self.not_found("transporte_gnre")
            self.click_relative(582, 130)
            self.tab()
            x=0
            while x<1:
                if not self.find( "transporte_tipoPFX", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_tipoPFX")
                self.click_relative(117, 205)
                self.type_down()
                self.enter()
                x=x+1
            if not self.find( "transporte_arquivos", matching=0.97, waiting_time=10000):
                self.not_found("transporte_arquivos")
            self.click_relative(572, 198)
            if not self.find( "transporte_seguraca_windows", matching=0.97, waiting_time=10000):
                self.not_found("transporte_seguraca_windows")
            self.click_relative(111, 328)
            self.tab()
            self.type_keys_with_interval(1,"1234")
            if not self.find( "transporte_pastadeschemas", matching=0.97, waiting_time=10000):
                self.not_found("transporte_pastadeschemas")
            self.click_relative(453, 267)
            if not self.find( "transporte_closepast", matching=0.97, waiting_time=10000):
                self.not_found("transporte_closepast")
            self.click_relative(300, 7)
            if not self.find( "transporte_pasttwo", matching=0.97, waiting_time=10000):
                self.not_found("transporte_pasttwo")
            self.click_relative(909, 264)
            if not self.find( "transporte_closepast_02", matching=0.97, waiting_time=10000):
                self.not_found("transporte_closepast_02")
            self.click_relative(298, 7)
            x=0
            while x<2:
                if not self.find( "transporte_ambiente", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_ambiente")
                self.click_relative(1221, 266)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<3:    
                 if not self.find( "transporte_imprimir", matching=0.97, waiting_time=10000):
                     self.not_found("transporte_imprimir")
                 self.click_relative(1291, 261)
                 self.type_down()
                 self.enter()
                 x=x+1 
            if not self.find( "transporte_salvar_cadastro", matching=0.97, waiting_time=10000):
                self.not_found("transporte_salvar_cadastro")
            self.click_relative(291, 40)
            if not self.find( "Transporte_cadastroretornar", matching=0.97, waiting_time=10000):
                 self.not_found("Transporte_cadastroretornar")
            self.click_relative(43, 40)
            self.click()
            ##########################################################################
            #grupo de empresa
            if not self.find( "transporte_grupo_de_empresa_02", matching=0.97, waiting_time=10000):
                self.not_found("transporte_grupo_de_empresa_02")
            self.click_relative(38, 61)        
            if not self.find( "transporte_grupo_de_empresa_01", matching=0.97, waiting_time=10000):
                self.not_found("transporte_grupo_de_empresa_01")
            self.click_relative(91, 109)
            self.type_keys_with_interval(1,"001")
            if not self.find( "transporte_localizar_grupo_de_empresa", matching=0.97, waiting_time=10000):
                self.not_found("transporte_localizar_grupo_de_empresa")
            self.click_relative(106, 44)
            if not self.find( "transporte_incluir_empresa", matching=0.97, waiting_time=10000):
                self.not_found("transporte_incluir_empresa")
            self.click_relative(164, 45)
            self.type_keys_with_interval(1,"teste1234")
            if not self.find( "transporte_salvar_fé", matching=0.97, waiting_time=10000):
                self.not_found("transporte_salvar_fé")
            self.click()    
            if not self.find( "transporte_cadastro_de_grupo_de_empresas_Excluir", matching=0.97, waiting_time=10000):
                self.not_found("transporte_cadastro_de_grupo_de_empresas_Excluir")
            self.click()
            self.enter()
            if not self.find( "transporte_cadastroreturn", matching=0.97, waiting_time=10000):
                self.not_found("transporte_cadastroreturn")
            self.click_relative(25, 49)
            if not self.find( "transporte_return02", matching=0.97, waiting_time=10000):
                self.not_found("transporte_return02")
            self.click_relative(39, 40)
            if not self.find( "transporte_cadastros_paises", matching=0.97, waiting_time=10000):
                self.not_found("transporte_cadastros_paises")
            self.click_relative(32, 30)
            if not self.find( "transporte_parametros", matching=0.97, waiting_time=10000):
                self.not_found("transporte_parametros")
            self.click_relative(144, 81)
            if not self.find( "transporte_parametrosf9", matching=0.97, waiting_time=10000):
                self.not_found("transporte_parametrosf9")
            self.click_relative(452, 76)
            self.enter()
            if not self.find( "transporte_localizar_parametros", matching=0.97, waiting_time=10000):
                self.not_found("transporte_localizar_parametros")
            self.click_relative(98, 43)
            if not self.find( "transporte_incluir_cadastro", matching=0.97, waiting_time=10000):
               self.not_found("transporte_incluir_cadastro")
            self.click_relative(161, 48)
            self.wait(500)
            if not self.find( "nao_incluir_empresa", matching=0.97, waiting_time=10000):
                self.not_found("nao_incluir_empresa")
            self.click()
            x=0
            while x<4:
                if not self.find( "transporte_motorista", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_motorista")
                self.click_relative(477, 156)
                self.type_down()
                self.enter()
                x=x+1
            if not self.find( "transporte_selectmotorista", matching=0.97, waiting_time=10000):
               self.not_found("transporte_selectmotorista")
            self.click_relative(210, 174)
            self.tab()
            if not self.find( "transporte_total_conhecimento", matching=0.97, waiting_time=10000):
                self.not_found("transporte_total_conhecimento")
            self.click_relative(471, 178)
            if not self.find( "transporte_total_conhecimento02", matching=0.97, waiting_time=10000):
                self.not_found("transporte_total_conhecimento02")
            self.click_relative(177, 197)
            self.tab()
            if not self.find( "empresa_localizar_cod0018", matching=0.97, waiting_time=10000):
                self.not_found("empresa_localizar_cod0018")
            self.click_relative(87, 5)
            if not self.find( "select_cod0018", matching=0.97, waiting_time=10000):
                self.not_found("select_cod0018")
            self.click()
            if not self.find( "selecionar_cod0018", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_cod0018")
            self.click()
            x=0
            while x<1:
                if not self.find( "transporte_livros_Fiscais", matching=0.97, waiting_time=10000):
                       self.not_found("transporte_livros_Fiscais")
                self.click_relative(306, 226)
                self.type_up()
                self.enter()
                x=x+1
            self.tab()
            x=0
            while x<2:
                if not self.find( "transporte_pagar_contas", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_pagar_contas")
                self.click_relative(306, 249)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<3:
                if not self.find( "transporte_receber_contas", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_receber_contas")
                self.click_relative(306, 266)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<2:
                if not self.find( "transporte_conhecimentos", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_conhecimentos")
                self.click_relative(308, 302)
                self.type_up()
                self.enter()
                x=x+1
            x=0
            while x<2:
                if not self.find( "transporte_pedagio_fatura", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_pedagio_fatura")
                self.click_relative(302, 316)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<2:
                if not self.find( "transporte_ordem_carregamento", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_ordem_carregamento")
                self.click_relative(302, 337)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<2:
                if not self.find( "transporte_tarifa_peso", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_tarifa_peso")
                self.click_relative(306, 364)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<2:
                if not self.find( "transporte_financeiro_gerado", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_financeiro_gerado")
                self.click_relative(300, 385)
                self.type_up()
                self.enter()
                x=x+1
            x=0
            while x<2:
               if not self.find( "transporte_responsavel_gerado", matching=0.97, waiting_time=10000):
                   self.not_found("transporte_responsavel_gerado")
               self.click_relative(303, 409)
               self.type_down()
               self.enter()
               x=x+1
            x=0
            while x<2:
                if not self.find( "transporte_consultar_placa", matching=0.97, waiting_time=10000):
                      self.not_found("transporte_consultar_placa")
                self.click_relative(308, 432)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<2:
                if not self.find( "transporte_frete_cte", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_frete_cte")
                self.click_relative(307, 456)
                self.type_up()
                self.enter()
                x=x+1
            x=0
            while x<2:
                if not self.find( "transporte_valor_de_seguro", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_valor_de_seguro")
                self.click_relative(771, 226)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<3:
                if not self.find( "transporte_pedagio_motorista", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_pedagio_motorista")
                self.click_relative(850, 247)
                self.type_down()
                self.enter()
                x=x+1
            self.type_keys_with_interval(1,"1234")
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,"1234")
            x=0
            while x<2:
                if not self.find( "transporte_pis_cofins", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_pis_cofins")
                self.click_relative(767, 314)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<2:
                if not self.find( "transporte_conhecimento_eletronico", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_conhecimento_eletronico")
                self.click_relative(635, 338)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<2:
                if not self.find( "transporte_modo_de_envio", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_modo_de_envio")
                self.click_relative(853, 337)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<2:
                if not self.find( "transporte_preventivo", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_preventivo")
                self.click_relative(641, 361)
                self.type_up()
                self.enter()
                x=x+1
            x=0
            while x<2:
                if not self.find( "transporte_frete_subcontratado", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_frete_subcontratado")
                self.click_relative(375, 10)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<3:
                if not self.find( "transporte_preventiva_atrasada", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_preventiva_atrasada")
                self.click_relative(770, 413)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<2:
                if not self.find( "transporte_entrega_em_branco", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_entrega_em_branco")
                self.click_relative(634, 433)
                self.type_down()
                self.enter()
                x=x+1
                #####################################################################################
                #gabiarra
            if not self.find( "empresa_pesquisar", matching=0.97, waiting_time=10000):
                self.not_found("empresa_pesquisar")
            self.click_relative(98, 10)
            self.type_keys_with_interval(1,"0021")
            if not self.find( "selecionar_code0021", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_code0021")
            self.click()
            if not self.find( "salvar_cadastro", matching=0.97, waiting_time=10000):
                self.not_found("salvar_cadastro")
            self.click()
            if not self.find( "transporte_formularios_parametros", matching=0.97, waiting_time=10000):
                self.not_found("transporte_formularios_parametros")
            self.click_relative(91, 115)
            if not self.find( "transporte_paramentros_incluir", matching=0.97, waiting_time=10000):
                self.not_found("transporte_paramentros_incluir")
            self.click_relative(27, 180)
            self.type_keys_with_interval(1,"123")
            self.tab()
            self.type_keys_with_interval(1,"12")
            self.tab()
            self.type_keys_with_interval(1,"2222")
            #x=0
            #while x<3:
                #if not self.find( "transporte_modelo_01", matching=0.97, waiting_time=10000):
                    #self.not_found("transporte_modelo_01")
               #self.click_relative(449, 194)
                #self.type_down()
                #self.enter()
                #x=x+1
                #
            
            x=0
            while x<1:
                if not self.find( "transporte_alterar_a_numeracao", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_alterar_a_numeracao")
                self.click_relative(92, 31)
                self.type_down()
                self.enter()
                x=x+1
            
            if not self.find( "transporte_confirmar_cadastro_003", matching=0.97, waiting_time=10000):
                self.not_found("transporte_confirmar_cadastro_003")
            self.click_relative(20, 270)
            if not self.find( "transporte_exluir_conheciment0s", matching=0.97, waiting_time=10000):
                self.not_found("transporte_exluir_conheciment0s")
            self.click()
            if not self.find( "transporte_sim_excluir", matching=0.97, waiting_time=10000):
                self.not_found("transporte_sim_excluir")
            self.click()
            if not self.find( "cadastro_MDFe", matching=0.97, waiting_time=10000):
                self.not_found("cadastro_MDFe")
            self.click()
            if not self.find( "transporte_incluir_parametros_01", matching=0.97, waiting_time=10000):
                self.not_found("transporte_incluir_parametros_01")
            self.click()
            self.type_keys_with_interval(1,"1123")
            self.tab()
            self.type_keys_with_interval(1,"999")
            ############################################
            #documentação
            
            if not self.find( "transporte_fechar_operacao_0-023", matching=0.97, waiting_time=10000):
                self.not_found("transporte_fechar_operacao_0-023")
            self.click()
            if not self.find( "transporte_numeracao_doc", matching=0.97, waiting_time=10000):
                self.not_found("transporte_numeracao_doc")
            self.click()
            if not self.find( "transporte_numero_ordem_abastecimento", matching=0.97, waiting_time=10000):
                self.not_found("transporte_numero_ordem_abastecimento")
            self.click_relative(174, 5)
            if not self.find( "transporte_paramentro_codigo_padroes", matching=0.97, waiting_time=10000):
                self.not_found("transporte_paramentro_codigo_padroes")
            self.click_relative(169, 108)
            if not self.find( "transporte_operacao_conhecimento", matching=0.97, waiting_time=10000):
                self.not_found("transporte_operacao_conhecimento")
            self.click()
            self.type_keys_with_interval(1,"0048")
            if not self.find( "transporte_selecionar_consultas_de_operacoes", matching=0.97, waiting_time=10000):
                self.not_found("transporte_selecionar_consultas_de_operacoes")
            self.click()
            if not self.find( "transporte_combustivel", matching=0.97, waiting_time=10000):
                self.not_found("transporte_combustivel")
            self.click()
            self.type_keys_with_interval(1,"001")
            if not self.find( "transporte_bomba_combustivel", matching=0.97, waiting_time=10000):
                self.not_found("transporte_bomba_combustivel")
            self.click_relative(53, 28)
            if not self.find( "transporte_selecionar_", matching=0.97, waiting_time=10000):
                self.not_found("transporte_selecionar_")
            self.click()
            if not self.find( "transporte_mao_de_obra", matching=0.97, waiting_time=10000):
                self.not_found("transporte_mao_de_obra")
            self.click()
            self.type_keys_with_interval(1,"01")
            if not self.find( "transporte_selecionar_consultas_de_itens_mao_de_obra", matching=0.97, waiting_time=10000):
                self.not_found("transporte_selecionar_consultas_de_itens_mao_de_obra")
            self.click()
            if not self.find( "transporte_cliente_fornecedor", matching=0.97, waiting_time=10000):
                self.not_found("transporte_cliente_fornecedor")
            self.click_relative(61, 34)
            if not self.find( "transporte_localizar_cliente", matching=0.97, waiting_time=10000):
                self.not_found("transporte_localizar_cliente")
            self.click()
            self.type_keys_with_interval(1,"3998")
            self.enter()
            if not self.find( "transporte_selecionar_joel_zanardini_andrade", matching=0.97, waiting_time=10000):
                self.not_found("transporte_selecionar_joel_zanardini_andrade")
            self.click()
            if not self.find( "transporte_tipo_de_pagamento_pedagio", matching=0.97, waiting_time=10000):
                self.not_found("transporte_tipo_de_pagamento_pedagio")
            self.click_relative(54, 27)
            self.type_keys_with_interval(1,"002")           
            if not self.find( "transporte_selecionar_tipo_de_pagament0", matching=0.97, waiting_time=10000):
                self.not_found("transporte_selecionar_tipo_de_pagament0")
            self.click()
            if not self.find( "transporte_operação_saida_de_abastecimento", matching=0.97, waiting_time=10000):
                self.not_found("transporte_operação_saida_de_abastecimento")
            self.click_relative(64, 27)
            self.type_keys_with_interval(1,"0048")
            self.wait(500)
            if not self.find( "transporte_consulta_de_ope", matching=0.97, waiting_time=10000):
                self.not_found("transporte_consulta_de_ope")
            self.click()
            if not self.find( "transporte_condicao_de_pagamento", matching=0.97, waiting_time=10000):
                self.not_found("transporte_condicao_de_pagamento")
            self.click_relative(48, 28)
            self.type_keys_with_interval(1,"0004")
            if not self.find( "transporte_selecionar_condicao_de_pagamento", matching=0.97, waiting_time=10000):
                self.not_found("transporte_selecionar_condicao_de_pagamento")
            self.click()
            self.tab()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,"12")
            #######################################################################################################################################
            #exportacao
            if not self.find( "transporte_parametro_exportacao", matching=0.97, waiting_time=10000):
                self.not_found("transporte_parametro_exportacao")
            self.click_relative(274, 109)
            self.tab()
            self.type_keys_with_interval(1,"250")
            self.tab()
            self.type_keys_with_interval(1,"300")
            self.tab()
            self.type_keys_with_interval(1,"350")
            self.tab()
            self.type_keys_with_interval(1,"400")
            self.tab()
            self.space()
            self.type_keys_with_interval(1,"450")
            if not self.find( "transporte_salvar_parametros", matching=0.97, waiting_time=10000):
                self.not_found("transporte_salvar_parametros")
            self.click()
            if not self.find( "transporte_exclii_parametros", matching=0.97, waiting_time=10000):
                self.not_found("transporte_exclii_parametros")
            self.click()      
            if not self.find( "transporte_confirmar_excluir_parametros", matching=0.97, waiting_time=10000):
                self.not_found("transporte_confirmar_excluir_parametros")
            self.click()
            if not self.find( "transporte_retornar_parametros", matching=0.97, waiting_time=10000):
                self.not_found("transporte_retornar_parametros")
            self.click()
            ###############################################################################
            #configuração de formularios
            if not self.find( "transporte_parametros_empresa", matching=0.97, waiting_time=10000):
                self.not_found("transporte_parametros_empresa")
            self.click()
            if not self.find( "transporte_parametr0s_01", matching=0.97, waiting_time=10000):
                self.not_found("transporte_parametr0s_01")
            self.click()
            if not self.find( "transporte_formularios_config", matching=0.97, waiting_time=10000):
                self.not_found("transporte_formularios_config")
            self.click()
            x=0
            while x<9:
                if not self.find( "transporte_configuracao_de_formularios_select", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_configuracao_de_formularios_select")
                self.click_relative(230, 149)
                self.type_down()
                self.enter()
                x=x+1
            self.type_right()
            self.tab()
            x=0
            while x<4:
                self.type_right()
                x=x+1
            self.tab()
            self.type_keys_with_interval(1,"310")
            self.tab()
            self.type_keys_with_interval(1,"210")
            #####################################################################
            #campos
            if not self.find( "transporte_configuracao_for", matching=0.97, waiting_time=10000):
                self.not_found("transporte_configuracao_for")
            self.click_relative(88, 73)
            if not self.find( "transporte_incluir_config_campos", matching=0.97, waiting_time=10000):
                self.not_found("transporte_incluir_config_campos")
            self.click()
            self.type_keys_with_interval(1,"jao13@#")
            self.tab()
            self.type_keys_with_interval(1,"_")
            self.tab()
            self.type_keys_with_interval(1,"205")
            self.tab()
            self.type_keys_with_interval(1,"30")
            self.tab()
            self.type_keys_with_interval(1,"00")
            self.tab()
            x=0
            while x<5:              
                if not self.find( "transporte_fonte_padrao", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_fonte_padrao")
                self.click_relative(71, 23)
                self.type_down()
                self.enter()
                x=x+1
            self.type_keys_with_interval(1,"25" )
            x=0
            while x<3:
                if not self.find( "transporte_tipo_de_campo", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_tipo_de_campo")
                self.click_relative(49, 20)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<3:
                if not self.find( "transporte_dados_dos_itens", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_dados_dos_itens")
                self.click_relative(116, 22)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<2:
                if not self.find( "transporte_local_de_empressao", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_local_de_empressao")
                self.click_relative(77, 20)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<20:
                if not self.find( "transporte_asteriscos", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_asteriscos")
                self.click_relative(138, 22)
                self.type_down()
                self.enter()
                x=x+1
            if not self.find( "transporte_gravar_campos", matching=0.97, waiting_time=10000):
                self.not_found("transporte_gravar_campos")
            self.click()
            if not self.find( "transporte_cancelar_campos", matching=0.97, waiting_time=10000):
                self.not_found("transporte_cancelar_campos")
            self.click()
            if not self.find( "transporte_excluir_campos", matching=0.97, waiting_time=10000):
                self.not_found("transporte_excluir_campos")
            self.click()
            if not self.find( "transporte_sim_confirmar_excluir_campos", matching=0.97, waiting_time=10000):
                self.not_found("transporte_sim_confirmar_excluir_campos")
            self.click()
            #########################################################################
            #lista
            if not self.find( "transporte_lista", matching=0.97, waiting_time=10000):
                self.not_found("transporte_lista")
            self.click_relative(146, 70)
            ###########################################################################
            #copiar configuracao
            if not self.find( "transporte_copiar_configuracao", matching=0.97, waiting_time=10000):
                self.not_found("transporte_copiar_configuracao")
            self.click_relative(198, 65)
            self.tab()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,"adasdas")
            if not self.find( "copiar_config", matching=0.97, waiting_time=10000):
                self.not_found("copiar_config")
            self.click()
            if not self.find( "transporte_confirmar_clonagem", matching=0.97, waiting_time=10000):
                self.not_found("transporte_confirmar_clonagem")
            self.click()
            ##################################################################
            #ajustes
            if not self.find( "transporte_ajustes", matching=0.97, waiting_time=10000):
                self.not_found("transporte_ajustes")
            self.click_relative(314, 66)
            self.type_keys_with_interval(1,"1234")
            self.tab()
            self.type_keys_with_interval(1,"12345")
            self.tab()
            self.type_keys_with_interval(1,"1232456")
            self.tab()
            self.type_keys_with_interval(1,"1235678")
            if not self.find( "transporte_ajustar", matching=0.97, waiting_time=10000):
                self.not_found("transporte_ajustar")
            self.click()
            if not self.find( "transporte_sim_ajustes", matching=0.97, waiting_time=10000):
                 self.not_found("transporte_sim_ajustes")
            self.click()
            if not self.find( "transporte_salvar_ajustes", matching=0.97, waiting_time=10000):
                self.not_found("transporte_salvar_ajustes")
            self.click()
            if not self.find( "transporte_cancelar_ajustes", matching=0.97, waiting_time=10000):
                self.not_found("transporte_cancelar_ajustes")
            self.click()
            self.wait(1000)
            if not self.find( "retornar_korobinsk_pagina_home", matching=0.97, waiting_time=10000):
                self.not_found("retornar_korobinsk_pagina_home")
            self.click()
            self.enter()
            self.enter()
            if not self.find( "transporte_cadastros_parametros_liberados_bloqueados", matching=0.97, waiting_time=10000):
                self.not_found("transporte_cadastros_parametros_liberados_bloqueados")
            self.click()
            if not self.find( "transporte_parametros_click", matching=0.97, waiting_time=10000):
                self.not_found("transporte_parametros_click")
            self.click()
            if not self.find( "transporte_liberacao_bloqueio", matching=0.97, waiting_time=10000):
                self.not_found("transporte_liberacao_bloqueio")
            self.click()
            if not self.find( "transporte_retornar_liberacao_de_periodosandblock", matching=0.97, waiting_time=10000):
                self.not_found("transporte_retornar_liberacao_de_periodosandblock")
            self.click()
            self.key_esc()
            if not self.find( "transporte_cadastro_aaaaaaa", matching=0.97, waiting_time=10000):
                self.not_found("transporte_cadastro_aaaaaaa")
            self.click()
            if not self.find( "parametros_transporte", matching=0.97, waiting_time=10000):
                self.not_found("parametros_transporte")
            self.click()
            if not self.find( "transporte_configurar_bombas", matching=0.97, waiting_time=10000):
                self.not_found("transporte_configurar_bombas")
            self.click()
            if not self.find( "transporte_cliente_agro", matching=0.97, waiting_time=10000):
                self.not_found("transporte_cliente_agro")
            self.click_relative(104, 7)
            if not self.find( "transporte_localizar_clientes_bombas", matching=0.97, waiting_time=10000):
                self.not_found("transporte_localizar_clientes_bombas")
            self.click()
            self.type_keys_with_interval(1,"3998")
            self.enter()
            self.type_down()
            if not self.find( "selecionar_cliente_bombas", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_cliente_bombas")
            self.click()
            if not self.find( "transporte_operacao_entrada", matching=0.97, waiting_time=10000):
                self.not_found("transporte_operacao_entrada")
            self.click_relative(153, 2)
            self.type_keys_with_interval(1,"0001")
            if not self.find( "transport_selecionar_operacao_entrada", matching=0.97, waiting_time=10000):
                self.not_found("transport_selecionar_operacao_entrada")
            self.click()
            if not self.find( "transporte_operacao_saida", matching=0.97, waiting_time=10000):
                self.not_found("transporte_operacao_saida")
            self.click_relative(147, 2)
            self.type_keys_with_interval(1,"0048")
            if not self.find( "transporte_selecionar_operacao_saida", matching=0.97, waiting_time=10000):
                self.not_found("transporte_selecionar_operacao_saida")
            self.click()
            if not self.find( "transporte_condicao_pagamento", matching=0.97, waiting_time=10000):
                self.not_found("transporte_condicao_pagamento")
            self.click_relative(148, 7)
            self.type_keys_with_interval(1,"0004")
            if not self.find( "transporte_selecionar_cond_pagamento", matching=0.97, waiting_time=10000):
                self.not_found("transporte_selecionar_cond_pagamento")
            self.click()
            if not self.find( "transporte_bico", matching=0.97, waiting_time=10000):
                self.not_found("transporte_bico")
            self.click_relative(48, 7)
            self.type_keys_with_interval(1,"123")
            if not self.find( "transport_bombinha", matching=0.97, waiting_time=10000):
                self.not_found("transport_bombinha")
            self.click_relative(86, 4)
            self.type_keys_with_interval(1,"001")
            if not self.find( "transporte_selecionar_bombinha", matching=0.97, waiting_time=10000):
                self.not_found("transporte_selecionar_bombinha")
            self.click()
            if not self.find( "transporte_incluir_bomba", matching=0.97, waiting_time=10000):
                self.not_found("transporte_incluir_bomba")
            self.click()
            if not self.find( "transporte_excluir_bomba", matching=0.97, waiting_time=10000):
                self.not_found("transporte_excluir_bomba")
            self.click()
            if not self.find( "Transporte_retornar_bomba", matching=0.97, waiting_time=10000):
                self.not_found("Transporte_retornar_bomba")
            self.click()
           ##############################################################################################################################################################################################
            #configurar WSDL
            if not self.find( "transporte_cadastro_config", matching=0.97, waiting_time=10000):
                self.not_found("transporte_cadastro_config")
            self.click()
            if not self.find( "transporte_parametros_config", matching=0.97, waiting_time=10000):
                self.not_found("transporte_parametros_config")
            self.click()
            if not self.find( "transporte_configuracao_wsdl", matching=0.97, waiting_time=10000):
                 self.not_found("transporte_configuracao_wsdl")
            self.click()
            if not self.find( "transporte_incluir_configuracao_wsld", matching=0.97, waiting_time=10000):
                self.not_found("transporte_incluir_configuracao_wsld")
            self.click()
            self.type_keys_with_interval(1,"teste$%")
            self.tab()
            self.type_keys_with_interval(1,"www.google.com")
            if not self.find( "transporte_tipo", matching=0.97, waiting_time=10000):
                self.not_found("transporte_tipo")
            self.click_relative(58, 26)
            self.type_down()
            self.enter()
            self.tab()
            self.type_keys_with_interval(1,"1234567890")
            if not self.find( "transporte_salvar_configuracao", matching=0.97, waiting_time=10000):
                self.not_found("transporte_salvar_configuracao")
            self.click()
            if not self.find( "transporte_excluir_configuracao", matching=0.97, waiting_time=10000):
                self.not_found("transporte_excluir_configuracao")
            self.click()
            if not self.find( "transporte_confirmar_excluir_config", matching=0.97, waiting_time=10000):
                self.not_found("transporte_confirmar_excluir_config")
            self.click()
            if not self.find( "incluir_configuracao_multi_CTE", matching=0.97, waiting_time=10000):
                self.not_found("incluir_configuracao_multi_CTE")
            self.click()
            self.tab()
            self.type_keys_with_interval(1,"teste")
            self.tab()
            self.type_keys_with_interval(1,"www.google.com")
            if not self.find( "transporte_tipo", matching=0.97, waiting_time=10000):
                self.not_found("transporte_tipo")
            self.click_relative(65, 27)
            if not self.find( "descriacao_create", matching=0.97, waiting_time=10000):
                self.not_found("descriacao_create")
            self.click_relative(23, 28)
            self.type_keys_with_interval(1,"descrição teste")
            self.tab()
            self.type_keys_with_interval(1,"url_teste")
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,"token_teste")

            if not self.find( "configuracao_multiCTE", matching=0.97, waiting_time=10000):
                self.not_found("configuracao_multiCTE")
            self.click()
            if not self.find( "excluir_registro_config", matching=0.97, waiting_time=10000):
                self.not_found("excluir_registro_config")
            self.click()
            if not self.find( "confirmar_excluir_config_certificado", matching=0.97, waiting_time=10000):
                self.not_found("confirmar_excluir_config_certificado")
            self.click()
            if not self.find( "fechar_multiCTE", matching=0.97, waiting_time=10000):
                self.not_found("fechar_multiCTE")
            self.click_relative(616, 11)
            if not self.find( "salvar_cte", matching=0.97, waiting_time=10000):
                self.not_found("salvar_cte")
            self.click()
            if not self.find( "retornar_menu_cadastr0_empresa", matching=0.97, waiting_time=10000):
                self.not_found("retornar_menu_cadastr0_empresa")
            self.click()
            if not self.find( "retornar_para_menu", matching=0.97, waiting_time=10000):
                self.not_found("retornar_para_menu")
            self.click()
            #############################################################################################
            #paises
            if not self.find( "transporte_cadastro", matching=0.97, waiting_time=10000):
                self.not_found("transporte_cadastro")
            self.click_relative(27, 27)
            if not self.find( "transporte_parametros_fiscais", matching=0.97, waiting_time=10000):
                self.not_found("transporte_parametros_fiscais")
            self.click_relative(77, 107)           
            if not self.find( "_transportes_Regionalizacao_001", matching=0.97, waiting_time=10000):
                self.not_found("_transportes_Regionalizacao_001")
            self.click()
            if not self.find( "transporte_paises", matching=0.97, waiting_time=10000):
                 self.not_found("transporte_paises")
            self.click()
            self.type_keys_with_interval(1,"brasil")
            if not self.find( "transporte_retornar_brasil", matching=0.97, waiting_time=10000):
                self.not_found("transporte_retornar_brasil")
            self.click()
            if not self.find( "transporte_cadastro_regioes", matching=0.97, waiting_time=10000):
                self.not_found("transporte_cadastro_regioes")
            self.click()
            self.type_down()
            self.type_down()
            self.type_down()
            #if not self.find( "transporte_parametros_fiscicais", matching=0.97, waiting_time=10000):
                #self.not_found("transporte_parametros_fiscicais")
            #self.click()
            self.enter()
            self.enter()
            self.type_down()
            self.enter()
            if not self.find( "Transporte_localizar_regioes", matching=0.97, waiting_time=10000):
                self.not_found("Transporte_localizar_regioes")
            self.click()
            if not self.find( "transporte_incluir_regioes", matching=0.97, waiting_time=10000):
                self.not_found("transporte_incluir_regioes")
            self.click()
            self.type_keys_with_interval(1,"regiao teste")
            if not self.find( "transporte_pais", matching=0.97, waiting_time=10000):
                self.not_found("transporte_pais")
            self.click_relative(70, 9)
            if not self.find( "transporte_localizar_regioes", matching=0.97, waiting_time=10000):
                self.not_found("transporte_localizar_regioes")
            self.click()
            if not self.find( "transporte_selecionar_regiao", matching=0.97, waiting_time=10000):
                self.not_found("transporte_selecionar_regiao")
            self.click()
            self.tab()
            self.tab()
            self.type_down()
            self.type_down()
            self.tab()
            self.type_down()
            self.type_down()
            if not self.find( "transporte_cancelar_regioneses", matching=0.97, waiting_time=10000):
                self.not_found("transporte_cancelar_regioneses")
            self.click()
            if not self.find( "transporte_confirmar_excluir_regiones", matching=0.97, waiting_time=10000):
                self.not_found("transporte_confirmar_excluir_regiones")
            self.click()
            if not self.find( "transporte_cadastro_de_regioes", matching=0.97, waiting_time=10000):
                self.not_found("transporte_cadastro_de_regioes")
            self.click_relative(15, 36)
            if not self.find( "transporte_cadastro_de_regioes", matching=0.97, waiting_time=10000):
                self.not_found("transporte_cadastro_de_regioes")
            self.click_relative(15, 36)
            ###########################################################################################################
            #estados
            if not self.find( "transporte_cadastro_parmetros_fisicais_0001", matching=0.97, waiting_time=10000):
                self.not_found("transporte_cadastro_parmetros_fisicais_0001")
            self.click()
            if not self.find( "transporte_parametros_fiscais_estados", matching=0.97, waiting_time=10000):
                self.not_found("transporte_parametros_fiscais_estados")
            self.click()
            if not self.find( "transporte_regionalizacao_estados", matching=0.97, waiting_time=10000):
                self.not_found("transporte_regionalizacao_estados")
            self.click()
            if not self.find( "transporte_estados_estado", matching=0.97, waiting_time=10000):
                self.not_found("transporte_estados_estado")
            self.click()
            if not self.find( "transporte_localizar_estado", matching=0.97, waiting_time=10000):
                self.not_found("transporte_localizar_estado")
            self.click()
            if not self.find( "transporte_incluir_estado", matching=0.97, waiting_time=10000):
                self.not_found("transporte_incluir_estado")
            self.click()
            self.type_keys_with_interval(1,"teste12$%")
            x=0
            while x<28:
                if not self.find( "transporte_sigla", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_sigla")
                self.click_relative(178, 5)
                self.type_down()
                self.enter()
                x=x+1
            if not self.find( "transporte_localizar_regiao", matching=0.97, waiting_time=10000):
                self.not_found("transporte_localizar_regiao")
            self.click_relative(87, 5)
            self.type_keys_with_interval(1,"001")
            if not self.find( "transporte_buscar_regiao", matching=0.97, waiting_time=10000):
                self.not_found("transporte_buscar_regiao")
            self.click()
            if not self.find( "transporte_selecionar_estado", matching=0.97, waiting_time=10000):
                self.not_found("transporte_selecionar_estado")
            self.click()
            x=0
            while x<27:
                if not self.find( "transporte_codigo_IBGE", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_codigo_IBGE")
                self.click_relative(206, 2)
                self.type_down()
                self.enter()
                x=x+1
            if not self.find( "regiao_selecionar", matching=0.97, waiting_time=10000):
                self.not_found("regiao_selecionar")
            self.click_relative(82, 12)
            self.type_keys_with_interval(1,"007")
            if not self.find( "selecionar_regiao", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_regiao")
            self.click()
            if not self.find( "transporte_salvar_regioes", matching=0.97, waiting_time=10000):
                self.not_found("transporte_salvar_regioes")
            self.click()
            if not self.find( "transporte_excluir_regiao", matching=0.97, waiting_time=10000):
                self.not_found("transporte_excluir_regiao")
            self.click()
            if not self.find( "transporte_regiao_confirmar_exclusao", matching=0.97, waiting_time=10000):
                self.not_found("transporte_regiao_confirmar_exclusao")
            self.click()
            if not self.find( "transporte_retornar_001234", matching=0.97, waiting_time=10000):
                self.not_found("transporte_retornar_001234")
            self.click()
            if not self.find( "transporte_cadastro_estados", matching=0.97, waiting_time=10000):
                self.not_found("transporte_cadastro_estados")
            self.click()
            self.type_keys_with_interval(1,"001")
            if not self.find( "transporte_retornar_cadastross_estados", matching=0.97, waiting_time=10000):
                self.not_found("transporte_retornar_cadastross_estados")
            self.click()        
            #if not self.find( "retornar_cadastro_empresa", matching=0.97, waiting_time=10000):
                #self.not_found("retornar_cadastro_empresa")
            #self.click_relative(16, 36)
            if not self.find( "cadastrosss", matching=0.97, waiting_time=10000):
                self.not_found("cadastrosss")
            self.click()
            if not self.find( "transportes_parametros_ficais_02", matching=0.97, waiting_time=10000):
                self.not_found("transportes_parametros_ficais_02")
            self.click()
            if not self.find( "grupo_fiscal_itens", matching=0.97, waiting_time=10000):
                self.not_found("grupo_fiscal_itens")
            self.click()
            if not self.find( "localizar_grupo_de_itens", matching=0.97, waiting_time=10000):
                self.not_found("localizar_grupo_de_itens")
            self.click()
            if not self.find( "incluir_grupo_de_itens", matching=0.97, waiting_time=10000):
                self.not_found("incluir_grupo_de_itens")
            self.click()
            self.type_keys_with_interval(1,"teste#$")
            if not self.find( "aliquota_interra", matching=0.97, waiting_time=10000):
                self.not_found("aliquota_interra")
            self.click_relative(168, 5)
            self.type_keys_with_interval(1,"123")
            if not self.find( "salvar_grupo_de_itens", matching=0.97, waiting_time=10000):
                self.not_found("salvar_grupo_de_itens")
            self.click()
            if not self.find( "retornar_cod_037", matching=0.97, waiting_time=10000):
                self.not_found("retornar_cod_037")
            self.click()
            self.click()
            ###############################################
            self.wait(1000)
            if not self.find( "transporte_cadastros_0003", matching=0.97, waiting_time=10000):
                self.not_found("transporte_cadastros_0003")
            self.click()
            if not self.find( "parametros_fiscais_00012", matching=0.97, waiting_time=10000):
                self.not_found("parametros_fiscais_00012")
            self.click()
            #################################################################################################
            #codigo de operações
            if not self.find( "transporte_codigo_operacao", matching=0.97, waiting_time=10000):
                self.not_found("transporte_codigo_operacao")
            self.click()
            if not self.find( "localizar_cod_operacao", matching=0.97, waiting_time=10000):
                self.not_found("localizar_cod_operacao")
            self.click()
            if not self.find( "incluir_cod_operacao", matching=0.97, waiting_time=10000):
                self.not_found("incluir_cod_operacao")
            self.click()
            if not self.find( "nao", matching=0.97, waiting_time=10000):
                self.not_found("nao")
            self.click()
            self.type_keys_with_interval(1,"teste#$")
            self.tab()
            self.type_up()
            self.tab()
            self.type_down()
            self.type_up()
            self.tab()
            self.tab()
            self.type_up()
            x=0
            while x<2:
                if not self.find( "operacao_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("operacao_estoque")
                self.click()
                self.type_down()
                self.enter()
                x=x+1
            if not self.find( "click_botton_up", matching=0.97, waiting_time=10000):
                self.not_found("click_botton_up")
            self.click()
            self.click()
            self.click()
            x=0
            while x<32:
                if not self.find( "tipo_de_movimentacao", matching=0.97, waiting_time=10000):
                        self.not_found("tipo_de_movimentacao")
                self.click_relative(208, 30)
                self.type_down()
                self.enter()
                x=x+1
            self.tab()
            x=0
            while x<8:
                if not self.find( "valor_de_movimentacao", matching=0.97, waiting_time=10000):
                    self.not_found("valor_de_movimentacao")
                self.click_relative(101, 28)
                self.type_up()
                self.enter()
                x=x+1
            x=0
            while x<3:
                if not self.find( "subtalizacao_notas", matching=0.97, waiting_time=10000):
                    self.not_found("subtalizacao_notas")
                self.click_relative(86, 31)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<2:
                if not self.find( "tipo_do_emitente", matching=0.97, waiting_time=10000):
                    self.not_found("tipo_do_emitente")
                self.click_relative(140, 30)
                self.type_down()
                self.enter()
                x=x+1            
            x=0
            while x<2:
                if not self.find( "tipo_lancto_dmed", matching=0.97, waiting_time=10000):
                    self.not_found("tipo_lancto_dmed")
                self.click_relative(106, 33)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<3:
                if not self.find( "tipo_de_documento_EFD", matching=0.97, waiting_time=10000):
                    self.not_found("tipo_de_documento_EFD")
                self.click_relative(108, 29)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<2:
                if not self.find( "tipo_controle_consulado", matching=0.97, waiting_time=10000):
                    self.not_found("tipo_controle_consulado")
                self.click_relative(146, 30)
                self.type_up()
                self.enter()
                x=x+1
            x=0
            while x<5:
                if not self.find( "natureza_municipal", matching=0.97, waiting_time=10000):
                    self.not_found("natureza_municipal")
                self.click_relative(159, 31)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<6:
                if not self.find( "indicador_da_natureza", matching=0.97, waiting_time=10000):
                     self.not_found("indicador_da_natureza")
                self.click_relative(206, 27)
                self.type_down()
                self.enter()
                x=x+1
            if not self.find( "indicador_de_empresa", matching=0.97, waiting_time=10000):
                self.not_found("indicador_de_empresa")
            self.click_relative(209, 28)
            if not self.find( "nao_se_aplica", matching=0.97, waiting_time=10000):
                self.not_found("nao_se_aplica")
            self.click()  
            x=0
            while x<7:
                if not self.find( "indicador_de_empresa", matching=0.97, waiting_time=10000):
                    self.not_found("indicador_de_empresa")
                self.click_relative(209, 28)
                self.type_down()
                self.enter() 
                x=x+1
            self.type_keys_with_interval(1,"12345")
            x=0
            while x<7:
                if not self.find( "custo_pedido_nota", matching=0.97, waiting_time=10000):
                     self.not_found("custo_pedido_nota")
                self.click_relative(122, 26)
                self.type_up()
                self.enter()
                x=x+1
            x=0
            while x<3:
                if not self.find( "tipo_funrual", matching=0.97, waiting_time=10000):
                     self.not_found("tipo_funrual")
                self.click_relative(112, 29)
                self.type_up()
                self.enter()
                x=x+1
            self.type_keys_with_interval(1,"333")
            x=0
            while x<3:
                if not self.find( "tipo_senar_e_aliquota", matching=0.97, waiting_time=10000):
                    self.not_found("tipo_senar_e_aliquota")
                self.click_relative(112, 27)
                self.type_down()
                self.enter()
                x=x+1
            self.type_keys_with_interval(1,"332")
            #if not self.find( "quota_capital_FETHAB", matching=0.97, waiting_time=10000):
                #self.not_found("quota_capital_FETHAB")
            #self.click_relative(112, 26)
           #self.type_up()
            x=0
            while x<3:
                if not self.find( "quota_capital_FETHAB", matching=0.97, waiting_time=10000):
                    self.not_found("quota_capital_FETHAB")
                self.click_relative(112, 26)
                self.type_down()
                self.enter()
                x=x+1
            self.type_keys_with_interval(1,"33")
            if not self.find( "tipo_desp_adm", matching=0.97, waiting_time=10000):
                self.not_found("tipo_desp_adm")
            self.click_relative(106, 25)
            self.type_up()
            x=0
            while x<3:
                if not self.find( "tipo_desp_adm", matching=0.97, waiting_time=10000):
                    self.not_found("tipo_desp_adm")
                self.click_relative(106, 25)
                self.type_down()
                self.enter()
                x=x+1
            self.type_keys_with_interval(1,"22")
            self.tab()
            self.type_keys_with_interval(1,"11")
            self.tab() 
            self.type_keys_with_interval(1,"44")
            self.tab()
            self.type_keys_with_interval(1,"55")
            x=0
            while x<4:
                if not self.find( "transporte_calcular_icms_simples", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_calcular_icms_simples")
                self.click_relative(101, 24)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<6:
                if not self.find( "transporte_pis_cofins_natureza", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_pis_cofins_natureza")
                self.click_relative(261, 24)
                self.type_down()
                self.enter()
                x=x+1 
            x=0
            while x<2:
                if not self.find( "pis_cofins_natureza", matching=0.97, waiting_time=10000):
                    self.not_found("pis_cofins_natureza")
                self.click_relative(190, 26)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<4:
                if not self.find( "transporte_frete", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_frete")
                self.click_relative(49, 27)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<4:
                    if not self.find( "transport_seguro", matching=0.97, waiting_time=10000):
                        self.not_found("transport_seguro")
                    self.click_relative(146, 27)
                    self.type_down()
                    self.enter()
                    x=x+1
            x=0
            while x<4:
                if not self.find( "outras_transportes", matching=0.97, waiting_time=10000):
                    self.not_found("outras_transportes")
                self.click_relative(151, 29)
                self.type_down()
                self.enter()
                x=x+1
            self.wait(1000)
            x=0
            while x<4:
                if not self.find( "transporte_frete_002", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_frete_002")
                self.click_relative(137, 26)
                self.type_up()
                self.enter()
                x=x+1
            x=0
            while x<4:
                if not self.find( "transporte_seguro_002", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_seguro_002")
                self.click_relative(43, 36)
                self.type_up()
                self.enter()
                x=x+1
            x=0
            while x<4:
                if not self.find( "contabiliza_serviço", matching=0.97, waiting_time=10000):
                    self.not_found("contabiliza_serviço")
                self.click_relative(233, 30)
                self.type_down()
                self.enter()
                x=x+1
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.type_keys_with_interval(1,"123123")
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            if not self.find( "transporte_dados_adicionais", matching=0.97, waiting_time=10000):
                self.not_found("transporte_dados_adicionais")
            self.click()
            if not self.find( "CFOP_padrao_do_moivmento", matching=0.97, waiting_time=10000):
                self.not_found("CFOP_padrao_do_moivmento")
            self.click_relative(65, 30)
            self.type_keys_with_interval(1,"1.101")
            if not self.find( "transporte_selecionar_cfop", matching=0.97, waiting_time=10000):
                self.not_found("transporte_selecionar_cfop")
            self.click()
            if not self.find( "tabela_de_preço_localizar", matching=0.97, waiting_time=10000):
                self.not_found("tabela_de_preço_localizar")
            self.click_relative(63, 35)
            self.type_keys_with_interval(1,"0000")
            if not self.find( "transporte_selecionar_preco_tabela", matching=0.97, waiting_time=10000):
                self.not_found("transporte_selecionar_preco_tabela")
            self.click()
            self.backspace()
            if not self.find( "transporte_tabelo_precos_servicos", matching=0.97, waiting_time=10000):
                self.not_found("transporte_tabelo_precos_servicos")
            self.click_relative(60, 28)
            self.type_keys_with_interval(1,"0000")
            if not self.find( "transporte_selecionar_tabela_de_precos", matching=0.97, waiting_time=10000):
                self.not_found("transporte_selecionar_tabela_de_precos")
            self.click()
            self.backspace()
            x=0
            while x<2:
                if not self.find( "movimentacao_para_transportes", matching=0.97, waiting_time=10000):
                    self.not_found("movimentacao_para_transportes")
                self.click_relative(185, 29)
                self.type_down()
                self.enter()
                x=x+1
            self.type_keys_with_interval(1,"teste123")
            if not self.find( "transporte_click", matching=0.97, waiting_time=10000):
                self.not_found("transporte_click")
            self.click()
            if not self.find( "campos_cliente_fornecedores", matching=0.97, waiting_time=10000):
                self.not_found("campos_cliente_fornecedores")
            self.click()
            if not self.find( "transporte_clicar", matching=0.97, waiting_time=10000):
                self.not_found("transporte_clicar")
            self.click_relative(40, 9)
            if not self.find( "campo_d_vendedores", matching=0.97, waiting_time=10000):
                self.not_found("campo_d_vendedores")
            self.click()
            if not self.find( "campos_disponiveis", matching=0.97, waiting_time=10000):
                self.not_found("campos_disponiveis")
            self.click_relative(-14, 32)
            if not self.find( "campos_de_condicao_pagamento", matching=0.97, waiting_time=10000):
                self.not_found("campos_de_condicao_pagamento")
            self.click()
            if not self.find( "observacoes", matching=0.97, waiting_time=10000):
                self.not_found("observacoes")
            self.click()
            self.type_keys_with_interval(1,"edqeqr")
            if not self.find( "transporte_salvar_eeeeeeeeshahahahah", matching=0.97, waiting_time=10000):
                self.not_found("transporte_salvar_eeeeeeeeshahahahah")
            self.click()
            ####################################################################
            #operação codigos fisicais COFP
            if not self.find( "retornar_cadsatrO_codigo_operacao", matching=0.97, waiting_time=10000):
                self.not_found("retornar_cadsatrO_codigo_operacao")
            self.click()
            self.click()
            self.click()
            if not self.find( "cadastro_de_parametros_002", matching=0.97, waiting_time=10000):
                self.not_found("cadastro_de_parametros_002")
            self.click()
            if not self.find( "parametros_fiscais_cofp", matching=0.97, waiting_time=10000):
                self.not_found("parametros_fiscais_cofp")
            self.click()
            if not self.find( "codigos_cfop_az", matching=0.97, waiting_time=10000):
                self.not_found("codigos_cfop_az")
            self.click()
            if not self.find( "localizar_cfop", matching=0.97, waiting_time=10000):
                self.not_found("localizar_cfop")
            self.click()
            if not self.find( "incluir_cfop", matching=0.97, waiting_time=10000):
                self.not_found("incluir_cfop")
            self.click()
            self.type_keys_with_interval(1,"3333")
            self.tab()
            self.type_keys_with_interval(1,"teste123$%")
            self.tab()
            if not self.find( "transporte_localizar_lupa_cfop", matching=0.97, waiting_time=10000):
                self.not_found("transporte_localizar_lupa_cfop")
            self.click()
            if not self.find( "localizar_codigo_operacao_cfop", matching=0.97, waiting_time=10000):
                self.not_found("localizar_codigo_operacao_cfop")
            self.click()
            if not self.find( "selecionar_cfop_and_return", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_cfop_and_return")
            self.click()
            self.tab()
            
            self.type_keys_with_interval(1,"123")
            self.tab()
            self.type_keys_with_interval(1,"123")
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.type_keys_with_interval(1,"123")
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.space()
            self.tab()
            self.type_right()
            self.tab()
            self.type_right
            self.type_right 
            self.type_right                    
            if not self.find( "salvar_cadastro_cfop", matching=0.97, waiting_time=10000):
                self.not_found("salvar_cadastro_cfop")
            self.click()
            self.click()
            if not self.find( "excluir_cfop", matching=0.97, waiting_time=10000):
                self.not_found("excluir_cfop")
            self.click()
            if not self.find( "Sim_excluir_registro_cfop", matching=0.97, waiting_time=10000):
                self.not_found("Sim_excluir_registro_cfop")
            self.click()
            if not self.find( "transporte_retornar_cfop", matching=0.97, waiting_time=10000):
                self.not_found("transporte_retornar_cfop")
            self.click()
            self.click()
            if not self.find( "cadastro_decretos", matching=0.97, waiting_time=10000):
                self.not_found("cadastro_decretos")
            self.click()
            if not self.find( "parametros_fiscais_decretos", matching=0.97, waiting_time=10000):
                self.not_found("parametros_fiscais_decretos")
            self.click()
            if not self.find( "decretos_observacoes", matching=0.97, waiting_time=10000):
                self.not_found("decretos_observacoes")
            self.click()
            if not self.find( "localizar_decretos", matching=0.97, waiting_time=10000):
                self.not_found("localizar_decretos")
            self.click()
            self.type_keys_with_interval(1,"001")
            if not self.find( "transporte_incluir_carta_cobrança", matching=0.97, waiting_time=10000):
                self.not_found("transporte_incluir_carta_cobrança")
            self.click()
            self.type_keys_with_interval(1,"221")
            if not self.find( "click_decreto", matching=0.97, waiting_time=10000):
                self.not_found("click_decreto")
            self.click()
            
            self.type_keys_with_interval(1,"teste123$%")
            if not self.find( "cancelar_cadastro_decreto", matching=0.97, waiting_time=10000):
                self.not_found("cancelar_cadastro_decreto")
            self.click()
            if not self.find( "sim_cancelar_decreto", matching=0.97, waiting_time=10000):
                self.not_found("sim_cancelar_decreto")
            self.click()
            if not self.find( "transporte_retornar_decreto_002", matching=0.97, waiting_time=10000):
                self.not_found("transporte_retornar_decreto_002")
            self.click()
            self.click()
            ###################################################################################
            #situações
            if not self.find( "transporte_incluir_situacao", matching=0.97, waiting_time=10000):
                self.not_found("transporte_incluir_situacao")
            self.click_relative(35, 24)
            if not self.find( "parametros_fiscais_incluir_situations", matching=0.97, waiting_time=10000):
                self.not_found("parametros_fiscais_incluir_situations")
            self.click()
            if not self.find( "situacoes", matching=0.97, waiting_time=10000):
                self.not_found("situacoes")
            self.click()
            if not self.find( "localizar_situacao", matching=0.97, waiting_time=10000):
                self.not_found("localizar_situacao")
            self.click()
            if not self.find( "incluir_situacao", matching=0.97, waiting_time=10000):
                self.not_found("incluir_situacao")
            self.click()
            if not self.find( "operacao_situacao", matching=0.97, waiting_time=10000):
                self.not_found("operacao_situacao")
            self.click_relative(52, 31)
            if not self.find( "localizar_opercao_situacao", matching=0.97, waiting_time=10000):
                self.not_found("localizar_opercao_situacao")
            self.click()
            self.type_keys_with_interval(1,"0001")
            if not self.find( "selecionar_situacao", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_situacao")
            self.click()
            if not self.find( "regiao_situcao", matching=0.97, waiting_time=10000):
                self.not_found("regiao_situcao")
            self.click_relative(50, 29)
            if not self.find( "localizar_situ", matching=0.97, waiting_time=10000):
                self.not_found("localizar_situ")
            self.click()
            self.type_keys_with_interval(1,"001")
            if not self.find( "selecionar_situ_001", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_situ_001")
            self.click()
            if not self.find( "grupo_fiscal", matching=0.97, waiting_time=10000):
                self.not_found("grupo_fiscal")
            self.click_relative(52, 28)
            self.type_keys_with_interval(1,"062")
            if not self.find( "localizar_grupo_fiscal", matching=0.97, waiting_time=10000):
                self.not_found("localizar_grupo_fiscal")
            self.click()
            if not self.find( "selecionar_grupo_fiscal", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_grupo_fiscal")
            self.click()
            if not self.find( "icms_base_calculo", matching=0.97, waiting_time=10000):
                self.not_found("icms_base_calculo")
            self.click_relative(140, 73)
            self.type_keys_with_interval(1,"200")
            self.tab()
            self.type_keys_with_interval(1,"200")
            x=0
            while x<5:
                if not self.find( "tipo_tributado", matching=0.97, waiting_time=10000):
                    self.not_found("tipo_tributado")
                self.click_relative(303, 29)
                self.type_down()
                self.enter()
                x=x+1
            self.tab()
            self.type_keys_with_interval(1,"300")
            self.tab()
            x=0
            while x<3:
                if not self.find( "saldo_base_reduzido", matching=0.97, waiting_time=10000):
                    self.not_found("saldo_base_reduzido")
                self.click_relative(134, 33)
                self.type_down()
                self.enter()
                x=x+1
            self.tab()
            x=0
            while x<4:
                if not self.find( "modalidade", matching=0.97, waiting_time=10000):
                    self.not_found("modalidade")
                self.click_relative(296, 28)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<25:
                if not self.find( "situacao_tributaria", matching=0.97, waiting_time=10000):
                    self.not_found("situacao_tributaria")
                self.click_relative(298, 25)
                self.type_down()
                self.enter()
                x=x+1
            self.tab()
            self.type_keys_with_interval(1,"002")
            self.tab()
            self.type_keys_with_interval(1,"002")
            x=0
            while x<12:
                if not self.find( "Motivo_desoneracao", matching=0.97, waiting_time=10000):
                    self.not_found("Motivo_desoneracao")
                self.click_relative(296, 26)
                self.type_down()
                self.tab()
                x=x+1
            self.space()
            self.tab()
            self.space
            self.tab()
            self.space()
            self.tab()
            self.type_keys_with_interval(1,"001")     
            self.tab()
            self.space()
            x=0
            while x<5:
                 if not self.find( "dif_interno", matching=0.97, waiting_time=10000):
                     self.not_found("dif_interno")
                 self.click_relative(252, 29)
                 self.type_down()
                 self.tab()
                 x=x+1
            if not self.find( "mono_icms", matching=0.97, waiting_time=10000):
                self.not_found("mono_icms")
            self.click_relative(77, 35)
            self.type_keys_with_interval(1,"003")
            if not self.find( "mono_icms_ret", matching=0.97, waiting_time=10000):
                self.not_found("mono_icms_ret")
            self.click_relative(250, 34)
            self.type_keys_with_interval(1,"003")
            self.tab()
            self.type_keys_with_interval(1,"003")
            x=0
            while x<2:
                if not self.find( "motivo_redutor_mono", matching=0.97, waiting_time=10000):
                    self.not_found("motivo_redutor_mono")
                self.click_relative(160, 26)
                self.type_down()
                self.tab()
                x=x+1
            if not self.find( "base_de_calculo", matching=0.97, waiting_time=10000):
                self.not_found("base_de_calculo")
            self.click_relative(114, 27)
            self.type_keys_with_interval(1,"300")
            self.tab()
            self.type_keys_with_interval(1,"300")
            x=0
            while x<1:
                if not self.find( "st_no_total_documento", matching=0.97, waiting_time=10000):
                    self.not_found("st_no_total_documento")
                self.click_relative(134, 25)
                self.type_down()
                self.tab()
                x=x+1
            self.space()
            self.tab()
            x=0
            while x<5:
                if not self.find( "tipo_antecipacao(valida)", matching=0.97, waiting_time=10000):
                    self.not_found("tipo_antecipacao(valida)")
                self.click_relative(301, 32)
                self.type_down()
                self.tab()
                x=x+1
            
            """"
            x=0
            while x<3:
                    if not self.find( "transporte_sempre_perguntar", matching=0.97, waiting_time=10000):
                        self.not_found("transporte_sempre_perguntar")
                    self.click()
                    self.type_right
                    x=x+1
            x=0
            while x<2:
                   if not self.find( "transporte_codigo", matching=0.97, waiting_time=10000):
                       self.not_found("transporte_codigo")
                   self.click()
                   self.type_right()
                   x=x+1 
            x=0
            while x<2:
                    if not self.find( "transporte_ajustar_coluna", matching=0.97, waiting_time=10000):
                        self.not_found("transporte_ajustar_coluna")
                    self.click()
                    self.type_right()
                    x=x+1
            x=0
            while x<3:
                if not self.find( "transporte_incio_de_campo", matching=0.97, waiting_time=10000):
                    self.not_found("transporte_incio_de_campo")
                self.click()
                self.type_right()
                x=x+1
            self.tab()
            self.space()
            """
def not_found(self, label):
                
                print(f"Element not found: {label}")  
        
if __name__ == '__main__':
    Bot.main()




























