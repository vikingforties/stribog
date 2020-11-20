# stribog
Compare the correlation between soaring forecasts and the actual weather.

There are a couple of Holfuy.com stations reading live weather in the Yorkshire Dales now. They have an API that allows us to record weather readings but both stations are not actually at flying sites which presents the difficulty that what they're reading may not be representative of what's happening on an actual flying site. That can be remedied with actual experience.

What is more interesting is, whether the forecasts we rely on to make our decision to go out and fly then tally up with what happens in reality? The two could differ in a couple of ways; the forecasts could be off linearly but correlate well. Or they may have very weak correlation of wind speed or direction under certain circumstances.

This is a collection of scripts to get the data from Holfuy and forecast services like RASP Blipmap, Windy, Meteoblue, Met Office, BBC, Windfinder etc. Then ingest the data and use a correlate function to find out how well each forecast matched reality, Finally displaying it with some nice plots. The end result is that we should be able to boil all this down to a few heuristics or rules of thumb that pilots should be able to easily remember when they make their decision in the morning. e.g. The BBC always tends to over read by X in an easterly or RASP usually under estimates cloud build up in the SW of the Dales.

Feel free to use this project for your own ends, free flying, sailing or whatever.
