from botcity.core import DesktopBot

class Bot(DesktopBot):
        def action(self, execution=None):

            #Esse código tem o objetivo de facilitar o encontro dos arquivos para teste
            #Ele está separado por blocos, favor sempre deixar apenas um bloco sem ser comentado

            #Tudo está organizado em ordem Esquerda->Direita e Superior->Inferior
            #Também está sendo a ordem de desenvolvimento.


            #BASE USADA PARA TESTES: ICTUS (versão editada) - 0000024 (Disponível em: )

            
            #Sempre prestar atenção na base que está sendo utilizada, pois a visão computacional
            #é muito sensível, então qualquer mudança mínima de cor/fonte/tamanho faz diferença.
            
            ###########################################################################################
            #                                GESTÃO ADMINISTRATIVA                                    #
            ###########################################################################################



            ###########################################################################################
            ###########################################################################################
            ###########################################################################################
            ###########################################################################################



            ###########################################################################################
            #                       CADASTRO DE EMPRESAS/GRUPO DE EMPRESAS                            #
            ###########################################################################################
            #aproximadamente 12 minutos e 40 segundos OK
            """
            self.execute(r"C:\Users\Rafael\Desktop\faturamento auto\Faturamento\Faturamento\bot.py")
            self.wait(1500)
            if not self.find( "executarpythonauto", matching=0.97, waiting_time=10000):
                self.not_found("executarpythonauto")
            if not self.find( "executararquivopython", matching=0.97, waiting_time=10000):
                self.not_found("executararquivopython")
            self.click()
            if not self.find( "voltarcontroletotal", matching=0.97, waiting_time=10000):
                self.not_found("voltarcontroletotal")
            self.click()
            self.wait(2000)
            """


            ###########################################################################################
            #                                 PARÂMETROS FISCAIS                                      #
            ###########################################################################################
            #aproximadamente 25 minutos OK
            """
            self.execute(r"C:\Users\Rafael\Desktop\faturamento auto\Faturamento\Faturamento\parametrosfiscais.py")
            self.wait(1500)
            if not self.find( "executarpythonauto", matching=0.97, waiting_time=10000):
                self.not_found("executarpythonauto")
            if not self.find( "executararquivopython", matching=0.97, waiting_time=10000):
                self.not_found("executararquivopython")
            self.click()
            if not self.find( "voltarcontroletotal", matching=0.97, waiting_time=10000):
                self.not_found("voltarcontroletotal")
            self.click()
            self.wait(2000)            
            """


            ###########################################################################################
            #                                 PARAMETROS FISCAIS 2                                    #
            ###########################################################################################
            #aproximadamente 17 minutos e 40 segundos OK
            """
            self.execute(r"C:\Users\Rafael\Desktop\faturamento auto\Faturamento\Faturamento\parametrosfiscais2.py")
            self.wait(1500)
            if not self.find( "executarpythonauto", matching=0.97, waiting_time=10000):
                self.not_found("executarpythonauto")
            if not self.find( "executararquivopython", matching=0.97, waiting_time=10000):
                self.not_found("executararquivopython")
            self.click()
            if not self.find( "voltarcontroletotal", matching=0.97, waiting_time=10000):
                self.not_found("voltarcontroletotal")
            self.click()
            self.wait(2000)
            """


            ###########################################################################################
            #                       CLIENTES, FORNECEDORES E TRANSPORTADORES                          #
            ###########################################################################################
            #aproximadamente 10 minutos OK ---------
            """
            self.execute(r"C:\Users\Rafael\Desktop\faturamento auto\Faturamento\Faturamento\clientes.py")
            self.wait(1500)
            if not self.find( "executarpythonauto", matching=0.97, waiting_time=10000):
                self.not_found("executarpythonauto")
            if not self.find( "executararquivopython", matching=0.97, waiting_time=10000):
                self.not_found("executararquivopython")
            self.click()
            if not self.find( "voltarcontroletotal", matching=0.97, waiting_time=10000):
                self.not_found("voltarcontroletotal")
            self.click()
            self.wait(2000)
            """


            ############################################################################################
            #                                    PARTE2CADASTROS                                       #
            ############################################################################################
            #aproximadamente 20 minutos OK 
            """
            self.execute(r"C:\Users\Rafael\Desktop\faturamento auto\Faturamento\Faturamento\Parte2Cadastros.py")
            self.wait(1500)
            if not self.find( "executarpythonauto", matching=0.97, waiting_time=10000):
                self.not_found("executarpythonauto")
            if not self.find( "executararquivopython", matching=0.97, waiting_time=10000):
                self.not_found("executararquivopython")
            self.click()
            if not self.find( "voltarcontroletotal", matching=0.97, waiting_time=10000):
                self.not_found("voltarcontroletotal")
            self.click()
            self.wait(2000)
            """


            ############################################################################################
            #                                    PARTE3CADASTROS                                       #
            ############################################################################################
            #aproximadamente 15 minutos OK 
            """
            self.execute(r"C:\Users\Rafael\Desktop\faturamento auto\Faturamento\Faturamento\Parte3Cadastros.py")
            self.wait(1500)
            if not self.find( "executarpythonauto", matching=0.97, waiting_time=10000):
                self.not_found("executarpythonauto")
            if not self.find( "executararquivopython", matching=0.97, waiting_time=10000):
                self.not_found("executararquivopython")
            self.click()
            if not self.find( "voltarcontroletotal", matching=0.97, waiting_time=10000):
                self.not_found("voltarcontroletotal")
            self.click()
            self.wait(2000)
            """


            ############################################################################################
            #                                   COMPRAS E VENDAS                                       #
            ############################################################################################
            #aproximadamente 23 minutos OK
            """
            self.execute(r"C:\Users\Rafael\Desktop\faturamento auto\Faturamento\Faturamento\compras.py")
            self.wait(1500)
            if not self.find( "executarpythonauto", matching=0.97, waiting_time=10000):
                self.not_found("executarpythonauto")
            if not self.find( "executararquivopython", matching=0.97, waiting_time=10000):
                self.not_found("executararquivopython")
            self.click()
            if not self.find( "voltarcontroletotal", matching=0.97, waiting_time=10000):
                self.not_found("voltarcontroletotal")
            self.click()
            self.wait(2000)
            """


            ############################################################################################
            #                                       MANUTENÇÕES                                        #
            ############################################################################################
            #aproximadamente 22 minutos OK 
            """
            self.execute(r"C:\Users\Rafael\Desktop\faturamento auto\Faturamento\Faturamento\manutencoes.py")
            self.wait(1500)
            if not self.find( "executarpythonauto", matching=0.97, waiting_time=10000):
                self.not_found("executarpythonauto")
            if not self.find( "executararquivopython", matching=0.97, waiting_time=10000):
                self.not_found("executararquivopython")
            self.click()
            if not self.find( "voltarcontroletotal", matching=0.97, waiting_time=10000):
                self.not_found("voltarcontroletotal")
            self.click()
            self.wait(2000)
            """


            ############################################################################################
            #                                          PREÇOS                                          #
            ############################################################################################
            #aproximadamente 21 minutos OK
            """
            self.execute(r"C:\Users\Rafael\Desktop\faturamento auto\Faturamento\Faturamento\precos.py")
            self.wait(1500)
            if not self.find( "executarpythonauto", matching=0.97, waiting_time=10000):
                self.not_found("executarpythonauto")
            if not self.find( "executararquivopython", matching=0.97, waiting_time=10000):
                self.not_found("executararquivopython")
            self.click()
            if not self.find( "voltarcontroletotal", matching=0.97, waiting_time=10000):
                self.not_found("voltarcontroletotal")
            self.click()
            self.wait(2000)
            """


            ############################################################################################
            #                                       RELATORIOS                                         #
            ############################################################################################
            #aproximadamente 27 minutos OK
            """
            self.execute(r"C:\Users\Rafael\Desktop\faturamento auto\Faturamento\Faturamento\relatorios.py")
            self.wait(1500)
            if not self.find( "executarpythonauto", matching=0.97, waiting_time=10000):
                self.not_found("executarpythonauto")
            if not self.find( "executararquivopython", matching=0.97, waiting_time=10000):
                self.not_found("executararquivopython")
            self.click()
            if not self.find( "voltarcontroletotal", matching=0.97, waiting_time=10000):
                self.not_found("voltarcontroletotal")
            self.click()
            self.wait(2000)
            """



            ############################################################################################
            #                                       RELATORIOS 2                                       #
            ############################################################################################
            #aproximadamente 24 minutos OK
            """
            self.execute(r"C:\Users\Rafael\Desktop\faturamento auto\Faturamento\Faturamento\relatorios2.py")
            self.wait(1500)
            if not self.find( "executarpythonauto", matching=0.97, waiting_time=10000):
                self.not_found("executarpythonauto")
            if not self.find( "executararquivopython", matching=0.97, waiting_time=10000):
                self.not_found("executararquivopython")
            self.click()
            if not self.find( "voltarcontroletotal", matching=0.97, waiting_time=10000):
                self.not_found("voltarcontroletotal")
            self.click()
            self.wait(2000)
            """


            ############################################################################################
            #                                          FINAL                                           #
            ############################################################################################
            #aproximadamente 10 minutos 
            """
            self.execute(r"C:\Users\Rafael\Desktop\faturamento auto\Faturamento\Faturamento\final.py")
            self.wait(1500)
            if not self.find( "executarpythonauto", matching=0.97, waiting_time=10000):
                self.not_found("executarpythonauto")
            if not self.find( "executararquivopython", matching=0.97, waiting_time=10000):
                self.not_found("executararquivopython")
            self.click()
            if not self.find( "voltarcontroletotal", matching=0.97, waiting_time=10000):
                self.not_found("voltarcontroletotal")
            self.click()
            self.wait(2000)
            """
            def not_found(self, label):
                print(f"Element not found: {label}")
if __name__ == '__main__':
    Bot.main()


