import curses
import functions

         
def main(stdscr):
    stdscr.addstr('Bem vindo ao validador/gerador de CPFs')
    stdscr.addstr('\nPara sair do programa a qualquer momento pressione ESC')
    stdscr.addstr('\n\nPressione qualquer tecla para continuar...')
    stdscr.getkey()
    
    while True:
        # defindo os padrões de cores
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        
        stdscr.clear()
        stdscr.addstr('- - - MENU - - -')
        stdscr.addstr('\n[1] - validar CPF')
        stdscr.addstr('\n[2] - Gerar CPF\n')
        stdscr.addstr('\nSua opção: ')
            
        choice = stdscr.getkey()
        
        if ord(choice) == 27:
            break

        elif choice != '1' and choice != '2':
            stdscr.clear()
            stdscr.addstr('Opção inválida.', curses.color_pair(2))
            stdscr.addstr('Pressione qualquer tecla para continuar...')
            stdscr.getkey()
        else:
            if choice == '1':
                stdscr.clear()
                cpf = functions.get_cpf(stdscr)
                if functions.validar(cpf):
                    stdscr.addstr(f'CPF analisado: {functions.formatar(cpf)}')
                    stdscr.addstr('\nO CPF válido', curses.color_pair(1))
                else:
                    stdscr.addstr(f'CPF analisado: {functions.formatar(cpf)}')
                    stdscr.addstr('\nCPF inválido', curses.color_pair(2))
                
            else:
                stdscr.clear()
                cpf_gerado = functions.gerar()
                stdscr.addstr(f'O CPF gerado foi: ')
                stdscr.addstr(cpf_gerado, curses.color_pair(1))
                
            stdscr.addstr('\n\nPressione qualquer tecla para voltar para o menu...')
            stdscr.getkey()

curses.wrapper(main)
