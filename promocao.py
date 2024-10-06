valor_do_desconto = int ( input ( 'qual o valor do desconto ? %'))
valor = float (input( 'qual o valor do produto ? R$') ) 
novo = valor - ( valor*valor_do_desconto /100)
print ( ' o produto que custava R${}, na promocao com desconto de {}% vai custar R${}' .format ( valor , valor_do_desconto, novo) )
valor_descontado = valor*valor_do_desconto/100
print ( ' o valor que foi descontado de R${} para R${} é R${} ' .format ( valor , novo , valor_descontado) ) 

