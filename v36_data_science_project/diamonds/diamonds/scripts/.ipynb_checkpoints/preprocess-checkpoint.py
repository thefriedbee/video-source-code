import os

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd


def hello_world():
    print("Hello World!")

#------below are methods loading the diamond dataset------
def load_data_from_seaborn():
    # the diamond dataset is contained in the seaborn package
    df = sns.load_dataset("diamonds")
    return df

def load_data_from_local(pth="../data_input/diamonds.csv"):
    df = pd.read_csv(pth, index_col=0)
    return df


#------below are methods for quality check, columns settings, ect.------
def print_diamond_basic_info(df):
    print("DataFrame head:")
    print(df.head(5))
    print("DataFrame samples:")
    print(df.sample(5))
    print("Check column types")
    print(df.dtypes)
    print("Describe distribution of number columns:")
    print(df.describe())
    print("Describe unique values for string columns:")
    print(df.value_counts())


def set_categorical_columns(df):
    from pandas.api.types import CategoricalDtype
    # types ordered from higher to lower quality
    clarity_type = CategoricalDtype(
        categories=["IF", "VVS1", "VVS2", "VS1", "VS2",
                    "SI1", "SI2", "I1"], ordered=True)
    color_type = CategoricalDtype(
        categories=["D", "E", "F", "G", "H", "I", "J"], ordered=True)
    cut_type = CategoricalDtype(
        categories=["Ideal", "Premium", "Very Good", "Good", "Fair"], ordered=True)
    
    df["clarity"] = df["clarity"].astype(clarity_type)
    df["color"] = df["color"].astype(clarity_type)
    df["cut"] = df["cut"].astype(clarity_type)


# ------below are methods for visualization------
def set_plot_style():
    plt.style.use('ggplot')
    # set font to Times New Roman
    plt.rcParams["font.family"] = "serif"
    plt.rcParams["font.serif"] = ["Times New Roman"]
    plt.rcParams["font.size"] = 20
    # set pixels per inches
    plt.rcParams['figure.dpi'] = 300


def plot_price_carat(df, ax=None):
    if ax is None:
        fig, ax = plt.subplots(1, 1, dpi=300, figsize=(16, 4))
    ax.plot(df.carat, df.price, "b+", alpha=0.2)
    ax.set_xlabel("weight (Carat)")
    ax.set_ylabel("price ($)")
    plt.xticks(np.arange(0, 5.5, 0.25))
    return ax


def plot_price_carat_seaborn(df, ax=None, hue="clarity"):
    if ax is None:
        fig, ax = plt.subplots(1, 1, dpi=300, figsize=(16, 4))
    # ax.plot(df.carat, df.price, "b+", alpha=0.2)
    sns.scatterplot(data=df, x="carat", y="price", 
                    hue=hue, ax=ax, alpha=0.2)
    ax.set_xlabel("weight (Carat)")
    ax.set_ylabel("price ($)")
    plt.xticks(np.arange(0, 5.5, 0.25))
    return ax


def plot_price_carat_facet(df):
    sea = sns.FacetGrid(
        df, row="clarity", col="color",
        margin_titles=True)
    sea.map(sns.scatterplot, "carat", "price")


# ------below are methods for selecting data------
def filt_by_cuts(df, cuts):
    filt = (df["cut"].isin(cut))
    df = df.loc[filt, :]
    return df

def filt_by_carat(df, carat_lb, carat_ub):
    filt = (df["carat"] >= carat_lb) & (df["carat"] <= carat_ub)
    df = df.loc[filt, :]
    return df

def filt_by_price(df, price_lb, price_ub):
    filt = (df["price"] >= price_lb) & (df["price"] <= price_ub)
    df = df.loc[filt, :]
    return df


# I like to write such processing object to organize the data pipeline
class DiamondPreprocess:
    def __init__(self, config_dict=None):
        if config_dict is None:
            config_dict = {
                "source": "local",  # either "local" or "seaborn"
                "carat_range": None,
                "cuts_types": [],
                "colors": [],
            }
        
        self.config = config_dict
        self.df = None
    
    def step0_load_dataset(self):
        source = self.config["source"]
        if source == "seaborn":
            self.df = load_data_from_seaborn()
        elif source == "seaborn":
            self.df = load_data_from_local()
        else:
            print("the source is not recognized")
            # consider to raise an Error if you want
            # raise Exception(f"the data source {source} is not recognized")
        
        # after loading the dataset, set the column types correctly
        set_categorical_columns()
    
    def step1_view_basic_info(self):
        print_diamond_basic_info(df)
    
    def step2_data_selection(self):
        # step 1-1. filter by carat
        (carat_lb, carat_ub) = self.config["carat_range"]
        df = filt_by_carat(df, carat_lb, carat_ub)
        
        # step 1-2. filter by cuts
        cuts_types = self.config["cuts"]
        df = filt_by_cuts(cuts_types)
        
        # step 2-3. filter by colors
        colors = self.config["colors"]
        df = filt_by_price(df)
        return df
    
    def step3_data_cleaning(self):
        pass
    
    def step4_data_transformation(self):
        pass
    
    def step5_export_outputs(self):
        self.df.to_csv("../data_output/diamonds_of_interest.csv")
    
    def pipeline(self):
        # just chain the methods step by step
        self.step0_load_dataset()
        self.step1_data_selection()
        self.step2_data_cleaning()
        self.step4_data_transformation()
        self.step5_export_outputs()


if __name__ == "main":
    # I use this place to test the functions above (examples of running the code)
    pass



