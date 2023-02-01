#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 20:08:33 2023

@author: sydneydolan
"""

## Code to check number of plays each month
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def get_monthrate(topsongs,csv_file):
    plays_per_month = np.zeros((len(topsongs),13))
    df = pd.read_csv(csv_file)
    sum_list =[]
    for i in range(len(topsongs)):

        sub_df = df[df['trackName'].eq(topsongs[i])]
        if sub_df.empty:
            sub_df = df[df['trackName'].str.contains(topsongs[i])]
        
        for index,row in sub_df['endTime'].iteritems():
            month = int(row[5:7])
            year = int(row[0:4])
            if month==1:
                if year ==2023:
                    plays_per_month[i,12] += 1
                else:
                    plays_per_month[i,month-1] += 1
            else:
                plays_per_month[i,month-1] += 1
        sum_list.append([str(sum(plays_per_month[i,:]))  ] )
    return plays_per_month,sum_list


def plot_top_song_month_rate(plays_per_month,topsongs,sum_list, sum_label):
    
        
    fig,axes  = plt.subplots(nrows=1,ncols=2,figsize = (12,8),dpi=650)
    ax = axes[0] #fig.add_subplot(121)
    ax2=axes[1]
    for i in range(len(topsongs)):
        if len(topsongs[i])>17 and len(topsongs[i])<=32:
            new_label = topsongs[i][0:17] +'\n' + topsongs[i][17:]
            ax.plot(np.linspace(0,13,13), plays_per_month[i,:], label = new_label)
            
        elif len(topsongs[i])>32 :
            new_label = topsongs[i][0:16] +'\n' + topsongs[i][16:32] + '\n' + topsongs[i][32:48] +'\n'+ topsongs[i][48:]
            ax.plot(np.linspace(0,13,13), plays_per_month[i,:], label = new_label)
            
            
        else:
            
            ax.plot(np.linspace(0,13,13), plays_per_month[i,:], label = topsongs[i])
        
    ax.set_ylabel('Number of Plays',fontsize=15)
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan']
    ax.set_xticks(np.linspace(0,13,13), months)
    ax.legend(bbox_to_anchor=(1.5, 0.90))
    ax.set_title('Number of Plays per Month\n for My Top Songs',fontsize =20)
    
    
    colLabels = ['# of Plays']

    
    tableData = sum_list
    
    ax2.set_axis_off()
    
    myTable = ax2.table(cellText=tableData, rowLabels=sum_label,colLabels=colLabels,
                       cellLoc='center', rowLoc='center', loc='center', bbox=[.75,.3,0.25,.60])
    
    
    myTable.auto_set_column_width(col=list(range(len(colLabels))))
    myTable.auto_set_font_size(False)
    myTable.set_fontsize(12)
    myTable.scale(1, 2)
    
    plt.show()




topsongs = ['Good Ones', 'On A Roll - Basic Tape Remix', 'Super Freaky Girl', 'Tongue - 12" Mix', 'Yes', 'DELUSIONAL', 'We like to Party!',     'Anima Libera','Like Me', 'Joypunks', 'Kitty Girl (feat. The Cast of Rupaul\'s Drag Race All Stars, Season 3)', 'Bodytalk (STFU)','CTRL + ALT + DEL', 'Get Up (Rattle)']
csv_path= 'Cleaned Spotify Full Year.csv'


plays_per_month,sum_list = get_monthrate(topsongs,csv_path)



topsongs_labels= ['Good Ones', 'On A Roll', 'Super Freaky Girl', 'Tongue - 12" Mix', 'Yes', 'DELUSIONAL', 'We like to Party!',     'Anima Libera','Like Me', 'Joypunks', 'Kitty Girl', 'Bodytalk (STFU)','CTRL + ALT + DEL', 'Get Up (Rattle)']
plot_top_song_month_rate(plays_per_month,topsongs,sum_list, topsongs_labels)
