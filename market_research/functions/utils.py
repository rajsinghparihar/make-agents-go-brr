def get_inventory(product_id: str, location: str):
    """
    fetch data from inventory table based on product_id and location as filter
    to make it more general we can create a function that fetches data from the appropriate table
    and then filters it based on a set of filters.
    """

    data = fetch_data(table_name)
    filtered_data = filter_data(
        data,
        filters={
            "product_id": product_id,
            "location": location,
        },  # here we will need to manage column names based on the data / table name
        # e.g. product_id might be called article or article_id in some table and something else in another table.
    )

    return filtered_data


def get_sales_data(date_range: tuple, breakdown: dict):
    """
    fetch data from sales or transactions table based on date_range and breakdown as filters (breakdown is a dictionary of additional filters)
    same as previous function, we can create a fetch data function that fetches data from the correct table
    and filters it based on date_range and breakdown
    """

    data = fetch_data(table_name)
    breakdown["start_date"] = date_range[0]
    breakdown["end_date"] = date_range[1]
    filtered_data = filter_data(data, filters=breakdown)

    return filtered_data


def get_customer_data(criteria: dict):
    """
    fetch data from customer table based on some criteria (filtering operation again)
    """

    data = fetch_data(table_name)
    filtered_data = filter_data(data, filters=criteria)

    return filtered_data


def get_product_price(product_id):
    pass


def get_competitor_price(product_name):
    pass


def calculate_sales_growth(period1, period2):
    pass


def recommend_products(customer_id):
    pass


def calculate_optimal_price(product_id, price_range):
    pass
