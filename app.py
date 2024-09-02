import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(layout='wide')

st.title('Ingresos del PGN')

ing = pd.read_csv('ingresos.csv')

st.dataframe(ing)

# composición

st.header("Evolución de la composición del ingreso")

hm = (ing
 .pivot_table(index='AÑO',
                     columns='TIPO DE INGRESOS',
                     values='valor_ingresos_pc',
                     aggfunc='sum')
                     .div(ing.pivot_table(index='AÑO',
                     columns='TIPO DE INGRESOS',
                     values='valor_ingresos_pc',
                     aggfunc='sum')
                     .sum(axis=1), axis=0))
hm_un = hm.unstack().reset_index()

fig = px.bar(hm_un, x='AÑO', y=0, color='TIPO DE INGRESOS' )

st.plotly_chart(fig)


fig = px.imshow(ing
 .pivot_table(index='AÑO',
                     columns='TIPO DE INGRESOS',
                     values='valor_ingresos_pc',
                     aggfunc='sum').T.div(1_000_000_000_000).round(2), text_auto=True, title='Composición del ingreso (billones de pesos)')

st.plotly_chart(fig)