from botcity.core import DesktopBot

class Bot(DesktopBot):
        def action(self, execution=None):

            #######################-----LOGIN-----############################
        
            self.execute(r"C:\Users\Rafael\Desktop\2207\faturamento.exe")
            
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

            ###################################################################
             
             
            if not self.find( "atalho_empresa", matching=0.97, waiting_time=10000):
                self.not_found("atalho_empresa")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "atalho_clientes", matching=0.97, waiting_time=10000):
                self.not_found("atalho_clientes")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "atalho_planocustos", matching=0.97, waiting_time=10000):
                self.not_found("atalho_planocustos")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "atalho_parametrosfiscais", matching=0.97, waiting_time=10000):
                self.not_found("atalho_parametrosfiscais")
            self.click_relative(26, 9)
            if not self.find( "atalho_regionalizacao1", matching=0.97, waiting_time=10000):
                self.not_found("atalho_regionalizacao1")
            self.click()
            if not self.find( "atalho_r_paises", matching=0.97, waiting_time=10000):
                self.not_found("atalho_r_paises")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "atalho_parametrosfiscais", matching=0.97, waiting_time=10000):
                self.not_found("atalho_parametrosfiscais")
            self.click_relative(26, 9)
            if not self.find( "atalho_regionalizacao1", matching=0.97, waiting_time=10000):
                self.not_found("atalho_regionalizacao1")
            self.click()
            if not self.find( "atalho_r_regioes", matching=0.97, waiting_time=10000):
                self.not_found("atalho_r_regioes")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "atalho_parametrosfiscais", matching=0.97, waiting_time=10000):
                self.not_found("atalho_parametrosfiscais")
            self.click_relative(26, 9)
            if not self.find( "atalho_regionalizacao1", matching=0.97, waiting_time=10000):
                self.not_found("atalho_regionalizacao1")
            self.click()
            if not self.find( "atalho_estados", matching=0.97, waiting_time=10000):
                self.not_found("atalho_estados")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "atalho_parametrosfiscais", matching=0.97, waiting_time=10000):
                self.not_found("atalho_parametrosfiscais")
            self.click_relative(26, 9)
            if not self.find( "atalho_regionalizacao1", matching=0.97, waiting_time=10000):
                self.not_found("atalho_regionalizacao1")
            self.click()
            if not self.find( "atalho_municipios", matching=0.97, waiting_time=10000):
                self.not_found("atalho_municipios")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "atalho_parametrosfiscais", matching=0.97, waiting_time=10000):
                self.not_found("atalho_parametrosfiscais")
            self.click_relative(26, 9)
            if not self.find( "atalho_grupoFiscalItens", matching=0.97, waiting_time=10000):
                self.not_found("atalho_grupoFiscalItens")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "atalho_parametrosfiscais", matching=0.97, waiting_time=10000):
                self.not_found("atalho_parametrosfiscais")
            self.click_relative(26, 9)
            if not self.find( "atalho_codigoFiscalCFOP", matching=0.97, waiting_time=10000):
                self.not_found("atalho_codigoFiscalCFOP")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "atalho_parametrosfiscais", matching=0.97, waiting_time=10000):
                self.not_found("atalho_parametrosfiscais")
            self.click_relative(26, 9)
            if not self.find( "atalho_importacaoNfeCFOP", matching=0.97, waiting_time=10000):
                self.not_found("atalho_importacaoNfeCFOP")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "atalho_parametrosfiscais", matching=0.97, waiting_time=10000):
                self.not_found("atalho_parametrosfiscais")
            self.click_relative(26, 9)
            if not self.find( "atalho_codigoOperacao", matching=0.97, waiting_time=10000):
                self.not_found("atalho_codigoOperacao")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "atalho_parametrosfiscais", matching=0.97, waiting_time=10000):
                self.not_found("atalho_parametrosfiscais")
            self.click_relative(26, 9)
            if not self.find( "atalho_decretosObsv", matching=0.97, waiting_time=10000):
                self.not_found("atalho_decretosObsv")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "atalho_parametrosfiscais", matching=0.97, waiting_time=10000):
                self.not_found("atalho_parametrosfiscais")
            self.click_relative(26, 9)
            if not self.find( "atalho_situacoes", matching=0.97, waiting_time=10000):
                self.not_found("atalho_situacoes")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "atalho_condicaoPagamento", matching=0.97, waiting_time=10000):
                self.not_found("atalho_condicaoPagamento")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "atalho_estoques", matching=0.97, waiting_time=10000):
                self.not_found("atalho_estoques")
            self.click_relative(26, 7)
            if not self.find( "atalho_familias", matching=0.97, waiting_time=10000):
                self.not_found("atalho_familias")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "atalho_estoques", matching=0.97, waiting_time=10000):
                self.not_found("atalho_estoques")
            self.click_relative(26, 7)
            if not self.find( "atalho_grupos", matching=0.97, waiting_time=10000):
                self.not_found("atalho_grupos")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "atalho_estoques", matching=0.97, waiting_time=10000):
                self.not_found("atalho_estoques")
            self.click_relative(26, 7)
            if not self.find( "atalho_subGrupos", matching=0.97, waiting_time=10000):
                self.not_found("atalho_subGrupos")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "atalho_estoques", matching=0.97, waiting_time=10000):
                self.not_found("atalho_estoques")
            self.click_relative(26, 7)
            if not self.find( "atalho_marcas", matching=0.97, waiting_time=10000):
                self.not_found("atalho_marcas")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "atalho_estoques", matching=0.97, waiting_time=10000):
                self.not_found("atalho_estoques")
            self.click_relative(26, 7)
            if not self.find( "atalho_itens", matching=0.97, waiting_time=10000):
                self.not_found("atalho_itens")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "atalho_estoques", matching=0.97, waiting_time=10000):
                self.not_found("atalho_estoques")
            self.click_relative(26, 7)
            if not self.find( "atalho_formulas", matching=0.97, waiting_time=10000):
                self.not_found("atalho_formulas")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "atalho_estoques", matching=0.97, waiting_time=10000):
                self.not_found("atalho_estoques")
            self.click_relative(26, 7)
            if not self.find( "atalho_cadeiaPrecos", matching=0.97, waiting_time=10000):
                self.not_found("atalho_cadeiaPrecos")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "atalho_estoques", matching=0.97, waiting_time=10000):
                self.not_found("atalho_estoques")
            self.click_relative(26, 7)
            if not self.find( "atalho_planoPrecos", matching=0.97, waiting_time=10000):
                self.not_found("atalho_planoPrecos")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "atalho_estoques", matching=0.97, waiting_time=10000):
                self.not_found("atalho_estoques")
            self.click_relative(26, 7)
            if not self.find( "atalho_vendedores", matching=0.97, waiting_time=10000):
                self.not_found("atalho_vendedores")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "atalho_bancos", matching=0.97, waiting_time=10000):
                self.not_found("atalho_bancos")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "atalho_contabil", matching=0.97, waiting_time=10000):
                self.not_found("atalho_contabil")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "atalho_compras", matching=0.97, waiting_time=10000):
                self.not_found("atalho_compras")
            self.click_relative(26, 8)
            if not self.find( "atalho_requisicoes", matching=0.97, waiting_time=10000):
                self.not_found("atalho_requisicoes")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "atalho_compras", matching=0.97, waiting_time=10000):
                self.not_found("atalho_compras")
            self.click_relative(26, 8)
            if not self.find( "atalho_cotacoes", matching=0.97, waiting_time=10000):
                self.not_found("atalho_cotacoes")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "atalho_compras", matching=0.97, waiting_time=10000):
                self.not_found("atalho_compras")
            self.click_relative(26, 8)
            if not self.find( "atalho_pedidos", matching=0.97, waiting_time=10000):
                self.not_found("atalho_pedidos")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "atalho_movEstoque", matching=0.97, waiting_time=10000):
                self.not_found("atalho_movEstoque")
            self.click_relative(25, 7)
            if not self.find( "atalho_entradaSaidaItens", matching=0.97, waiting_time=10000):
                self.not_found("atalho_entradaSaidaItens")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "atalho_movFinanceiro", matching=0.97, waiting_time=10000):
                self.not_found("atalho_movFinanceiro")
            self.click_relative(28, 8)
            if not self.find( "atalho_contasPagarReceber", matching=0.97, waiting_time=10000):
                self.not_found("atalho_contasPagarReceber")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "atalho_movFinanceiro", matching=0.97, waiting_time=10000):
                self.not_found("atalho_movFinanceiro")
            self.click_relative(28, 8)
            if not self.find( "atalho_remessaBancaria", matching=0.97, waiting_time=10000):
                self.not_found("atalho_remessaBancaria")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "atalho_movFinanceiro", matching=0.97, waiting_time=10000):
                self.not_found("atalho_movFinanceiro")
            self.click_relative(28, 8)
            if not self.find( "atalho_remessaSerasa", matching=0.97, waiting_time=10000):
                self.not_found("atalho_remessaSerasa")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "atalho_vendas", matching=0.97, waiting_time=10000):
                self.not_found("atalho_vendas")
            self.click_relative(29, 9)
            if not self.find( "atalho_pedidosVendas", matching=0.97, waiting_time=10000):
                self.not_found("atalho_pedidosVendas")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "atalho_vendas", matching=0.97, waiting_time=10000):
                self.not_found("atalho_vendas")
            self.click_relative(29, 9)
            if not self.find( "atalho_emissaoNotaFiscal", matching=0.97, waiting_time=10000):
                self.not_found("atalho_emissaoNotaFiscal")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "atalho_vendas", matching=0.97, waiting_time=10000):
                self.not_found("atalho_vendas")
            self.click_relative(29, 9)
            if not self.find( "atalho_romaneioSaida", matching=0.97, waiting_time=10000):
                self.not_found("atalho_romaneioSaida")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "atalho_vendas", matching=0.97, waiting_time=10000):
                self.not_found("atalho_vendas")
            self.click_relative(29, 9)
            if not self.find( "atalho_vendasBalcao", matching=0.97, waiting_time=10000):
                self.not_found("atalho_vendasBalcao")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "atalho_vendas", matching=0.97, waiting_time=10000):
                self.not_found("atalho_vendas")
            self.click_relative(29, 9)
            if not self.find( "atalhos_condicionais", matching=0.97, waiting_time=10000):
                self.not_found("atalhos_condicionais")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "atalho_vendas", matching=0.97, waiting_time=10000):
                self.not_found("atalho_vendas")
            self.click_relative(29, 9)
            if not self.find( "atalhos_orcamentos", matching=0.97, waiting_time=10000):
                self.not_found("atalhos_orcamentos")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "atalho_vendas", matching=0.97, waiting_time=10000):
                self.not_found("atalho_vendas")
            self.click_relative(29, 9)
            if not self.find( "atalhos_amostra", matching=0.97, waiting_time=10000):
                self.not_found("atalhos_amostra")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "atalho_vendas", matching=0.97, waiting_time=10000):
                self.not_found("atalho_vendas")
            self.click_relative(29, 9)
            if not self.find( "atalhos_checagemLancamento", matching=0.97, waiting_time=10000):
                self.not_found("atalhos_checagemLancamento")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "atalho_compromissos", matching=0.97, waiting_time=10000):
                self.not_found("atalho_compromissos")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "atalho_calculadora", matching=0.97, waiting_time=10000):
                self.not_found("atalho_calculadora")
            self.click()
            if not self.find( "fechar_calculadora", matching=0.97, waiting_time=10000):
                self.not_found("fechar_calculadora")
            self.click_relative(281, 9)
            if not self.find( "atalho_calendario", matching=0.97, waiting_time=10000):
                self.not_found("atalho_calendario")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "atalho_alterarData", matching=0.97, waiting_time=10000):
                self.not_found("atalho_alterarData")
            self.click()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
            
            

            
            


            def not_found(self, label):
                print(f"Element not found: {label}")  
if __name__ == '__main__':
    Bot.main()