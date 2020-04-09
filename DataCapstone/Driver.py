import FinanceProjectInteractive as fp

p = int(input('press 1 to INITIALISE the code. press 0 to exit: '))
if p == 1:
    fp.default()
    while True:
        print('WELCOME')
        print('***********************************************************')
        t = int(input(
            '1. print the highest closing value of each stock \n2. draw pair plots of closing price of all the '
            'stocks\n3. print the dataframe containing the date of worst and best single day return of each bank.\n4. '
            'print the standard deviation of the returns of all the banks\n 5. Draw distplot of returns of the '
            'sotcks\n6. draw line plot of closing value of all the stocks over the entire time period\n7. draw heat '
            'map of correlation data between the stocks\n8. draw clustermap of the correlation data between the '
            'stocks\n--->'))
        if t == 1:
            ch = fp.close_high()
            print(ch)
        elif t == 2:
            fp.draw_pair()
        elif t == 3:
            fp.dt_max_min()
        elif t == 4:
            fp.show_std()
        elif t == 5:
            stock = input('enter the stock ticker in upppercase: ')
            start = list(map(int, input('enter the start date in yyyy mm dd format: ').split()))
            end = list(map(int, input('enter the end date in yyyy mm dd format: ').split()))
            fp.draw_distplot(st=start, en=end, sto=stock)
        elif t == 6:
            fp.draw_lineplot()
        elif t == 7:
            fp.draw_heatmap()
        elif t== 8:
            fp.draw_clustermap()
        print('***************************')
        print('***************************')
        print('***************************')
        print('***************************')
        print('***************************')