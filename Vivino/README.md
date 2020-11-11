# Structure of Vivino dataset

## Keys of each row:
1 | vintage | id, name, rating_count, av_rating, reviews, labels?, certified, images, region, country, info_per_country, most_used_grapes, winery, winery_review, rank, rating_per_year with has_valid_ratings, alcohol_level, sweetness, body/acidity, wine_critic_scores, awards, rating_distribution, wine_facts, grapes
2 | price | id, vintage_id, price, currency, bottle_type, bottles_sold_count, volume_bottle
3 | highlights | price for oldest available, ratings, ranks, description of region, interesting facts, body/acidity, most_used_grapes_region, grapes
4 | merchant | name, description, country, #users, #wines, #wineries, most_used_grapes_in_country
5 | shipping_message | - 
6 | sold_out | True/False
7 | available_vintage_year | - 
8 | carts | -
9 | prices_and_availability | id, price, median_price, availability.vintage.year, price_per_merchant with bottles sold and bottle volume
10 | basic_user_vintage | -
11 | price_range | general filter. Should be the same
12 | is_deal_page | True/False


## Tables to be built
1. Prices_per_merchant
2. Merchants
3. Wines - ratings, basic info, wine_facts, grapes
4. Prices per wine - av, median
5. Regions
6. Countries
7. Wineries
8. rating_per_year with has_valid_ratings