
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns


# Utility functions for charts
def count_plot(df, x, hue=None, title='', palette=['#FF5A5F', '#00A699', '#FC642D', '#484848', '#767676']):
    plt.figure(figsize=(10, 6))
    sns.countplot(
        data=df,
        x=x,
        hue=hue,
        palette=palette,
        width=0.8,
        dodge=False
    )
    plt.title(title, color='#484848')
    plt.xticks(rotation=45)
    plt.tight_layout()
    return plt.gcf()

def bar_chart(data, x, y, title='', palette=['#FF5A5F', '#00A699', '#FC642D', '#484848', '#767676']):
    fig = px.bar(data, x=x, y=y, title=title, color_discrete_sequence=palette)
    return fig

def pie_chart(data, names, values, title='', palette=['#FF5A5F', '#00A699', '#FC642D', '#484848', '#767676']):
    fig = px.pie(data, names=names, values=values, title=title, color_discrete_sequence=palette)
    return fig

def violin_plot(df, x, y, title='', palette=['#FF5A5F', '#00A699', '#FC642D', '#484848', '#767676']):
    fig = px.violin(df, x=x, y=y, box=True, title=title, color_discrete_sequence=palette)
    return fig

def box_plot(df, x, y, color, hue, title='', palette=['#FF5A5F', '#00A699', '#FC642D', '#484848', '#767676'], category_orders=None):
    fig = px.box(df, x=x, y=y, color=color, title=title, color_discrete_sequence=palette, category_orders=category_orders)
    return fig

def scatter_plot(df, x, y, color=None, title='', palette=['#FF5A5F', '#00A699', '#FC642D', '#484848', '#767676']):
    fig = px.scatter(df, x=x, y=y, color=color, title=title, color_discrete_sequence=palette)
    return fig

def count_plot_swapped(df, x, hue=None, title='', palette=['#FF5A5F', '#00A699', '#FC642D', '#484848', '#767676']):
    plt.figure(figsize=(10, 10))
    ax = sns.countplot(
        data=df,
        y=x,  # Swap axes
        hue=hue,
        palette=palette,
        width=0.8,
        dodge=False
    )
    plt.title(title, color='#484848')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Move the x and y axes
    ax.spines['left'].set_position(('outward', 10))  # Move y-axis outward
    ax.spines['bottom'].set_position(('outward', 10))  # Move x-axis outward
    
    return plt.gcf()