FinanceAPI
==========

Script to extract data against Yahoo! Finance India

Yahoo! Finance allows to download stock data as csv file if you need. Sadly, this feature is discontinued in India. So, FinanceAPI fills the gap.

# Usage Policy
The script uses basic web scraping techniques to get data from Yahoo! Finance India. Please be aware that this is only for personal use. REDISTRIBUTION OR USE OF DATA MIGHT BE PROTECTED BY COPYRIGHT LAWS. The LICENSE file is valid for script only, not data.

# Install

1. `pip install pyquery`    
2. `pip install FinanceAPI`

# Usage
After the install, you can use as follows.

	import financeAPI as fa
	
	# get summery for today
	fa.get_summery('ICICIBANK')
	
	Out:
	{'date_time': '27 Sep 3:57PM',
    'max_price': 915.7,
    'min_price': 949.35,
    'previous_close': 945.15,
    'price': 923.3,
    'today_change': -21.85,
    'today_open': 949.0,
    'volume': 574265}
    
    # get today's quote
    
    fa.get_quote('ICICIBANK')
    
    Out: 923.3
    
Rest on Docstrings FTW :)