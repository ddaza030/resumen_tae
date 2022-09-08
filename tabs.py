import streamlit as st
from graficos_mtlp import *
from metadata import Texto


def tab_show(cluster, df):

    st.write(Texto.caract_per_clust[cluster]['grafica1'])
    carreras = {
         'CIP11BACHL': st.checkbox('CIP11BACHL' + ' '*cluster, value=True),
         'CIP14BACHL': st.checkbox('CIP14BACHL' + ' '*cluster),
         'CIP15BACHL': st.checkbox('CIP15BACHL' + ' '*cluster),
         'CIP27BACHL': st.checkbox('CIP27BACHL' + ' '*cluster),
    }
    carreras_show = [key for key, value in carreras.items() if value]
    st.pyplot(barplot_cat(df, cluster, carreras_show))

def continuas_show(df):
     options = st.multiselect(
        '¿Que cluster quieres comparar?',
        [0, 1, 2, 3],
        [0, 1, 2, 3])
    #clusters = [value for value in options.values()]
     option = st.selectbox(
        '¿Qué variable continua desea comparar?',
        ('DEBT_MDN','PCTFLOAN','GRAD_DEBT_MDN','PCIP11','PCIP15','PCIP14','PCIP27','PCTPELL'))

    #print(option)

   
    
     st.write(str(options))
     if(len(options) != 0):
          
          st.markdown('### Boxplot de una variable continua vs clusters seleccionados')
          st.pyplot(boxplot_cluster_vs_continuas(df,options,option))
          
          st.markdown('### Diagrama de densidad de una variable continua vs clusters seleccionados')
          st.pyplot(dens_plot_cluster_vs_continuas(df,options,option))

          st.markdown('### Diagrama de violin de una variable continua vs clusters seleccionados')
          st.pyplot(violin_plot_cluster_vs_continuas(df,options,option))
     else:     
          st.markdown("### Seleccione algún cluster")
     