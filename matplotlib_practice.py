import pandas as pd
from matplotlib import pyplot as plt


# --------------- Line graph showing website visitors ---------------

marketing_data = pd.read_csv('marketing_analytics.csv')

months = marketing_data['Month']
total_visitors = marketing_data['Total Website Visitors']
new_visitors = marketing_data['New Visitors']

plt.figure(figsize=(7, 5)) # shows size of figure in inches: width, height
plt.plot(months, total_visitors, label="Total Website Visitors", marker='o', color='green')
plt.plot(months, new_visitors, label="New Website Visitors", marker='o', color='blue')
plt.legend() # This shows line labels
plt.ylabel('# Website Visitors')
plt.title('Website Analytics - 2018')
#plt.show() # displays chart
#plt.savefig('website_visitor_analytics.png') # will save the file to your directory


# --------------- Stacked bar graph showing the breakdown of revenue ---------------

plt.close('all') # this first clears out the previous plots before we begin this next one.

revenue_data = pd.read_csv('q4_revenue.csv')

months = revenue_data['Month']
subscriptions = revenue_data['Subscriptions']
campaigns = revenue_data['Campaigns']

plt.figure(figsize=(7, 5))
plt.bar(months, subscriptions, label="Subscriptions", color = '#3e66e8')
plt.bar(months, campaigns, label="Campaigns", bottom = subscriptions, color = '#ff8c00')
plt.title('Revenue 2018: Subscriptions & Campaigns')
plt.ylabel('Total Revenue ($)')
plt.legend(loc =2)
#plt.show()
#plt.savefig('website_revenue.png') # will save the file to your directory

# --------------- Stacked bar graph showing the breakdown of revenue ---------------

plt.close('all') # this first clears out the previous plots before we begin this next one.

top_channels = pd.read_csv('top_channels.csv')
top_sources = pd.read_csv('top_sources.csv')

channels = top_channels['Channels']
channel_visitors = top_channels['Website Visitors']

sources = top_sources['Sources']
source_visitors = top_sources['Website Visitors']

plt.pie(channel_visitors, autopct='%0.2f%%', textprops={'fontsize': 12, 'color': 'black'})
plt.legend(channels)
plt.axis('equal')
#plt.show()
#plt.savefig('top_channels.png')

plt.close('all') # this first clears out the previous plots before we begin this next one.

plt.pie(source_visitors, autopct='%0.2f%%', textprops={'fontsize': 12, 'color': 'black'})
plt.legend(sources)
plt.axis('equal')
#plt.show()
#plt.savefig('top_sources.png')






