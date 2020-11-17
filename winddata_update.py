# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 09:43:51 2020

@author: Xiajie Jia
"""

from WindPy import *
import pandas as pd
from datetime import timedelta

w.start()
path = 'Wind/update'
tradedate = '2020-11-12'
code_list = []  

#更新全Acode信息
stock_code = w.wset("sectorconstituent","date={};sectorid=a001010100000000".format(tradedate))
df = pd.DataFrame(stock_code.Data).T
df.columns = stock_code.Fields
code_list = df.wind_code.unique().tolist()

#更新全A日频数据
stock_daily = w.wss(','.join(code_list), "open,high,low,close,volume,amt,dealnum,pct_chg,swing,vwap,adjfactor,turn,free_turn_n,maxup,maxdown,maxupordown,open_auction_price,open_auction_volume,open_auction_amount,\
                   ev,mkt_cap_ard,pe_ttm,val_pe_deducted_ttm,pb_lf,pb_mrq,ps_ttm,ps_lyr,pcf_ocf_ttm,pcf_ncf_ttm,pcf_ocflyr,pcf_nflyr,ev2,ev2_to_ebitda,mkt_freeshares",
                   "tradeDate={};priceAdj=U;cycle=D;unit=1".format(''.join(tradedate.split('-'))))
df_stock = pd.DataFrame(stock_daily.Data).T
df_stock.columns = [x.lower() for x in stock_daily.Fields]
df_stock.loc[:,'code'] = stock_daily.Codes
df_stock.loc[:,'date'] = pd.to_datetime(tradedate)

#更新index日频数据
index_daily = w.wss("000688.SH,000001.SH,000017.SH,399100.SZ,399101.SZ,399102.SZ,399106.SZ,399110.SZ,399120.SZ,399130.SZ,399131.SZ,399132.SZ,399133.SZ,399134.SZ,399135.SZ,399136.SZ,399137.SZ,399138.SZ,399139.SZ,399140.SZ,399150.SZ,399160.SZ,399170.SZ,399180.SZ,399190.SZ,399200.SZ,399210.SZ,399220.SZ,399230.SZ,399231.SZ,399232.SZ,399233.SZ,399234.SZ,399235.SZ,399236.SZ,399237.SZ,399238.SZ,399239.SZ,399240.SZ,399241.SZ,399242.SZ,399243.SZ,399244.SZ,399248.SZ,399249.SZ,000300.SH,000903.SH,000904.SH,000905.SH,000906.SH,000852.SH,000985.CSI,CI005001.WI,CI005002.WI,CI005003.WI,CI005004.WI,CI005005.WI,CI005006.WI,CI005007.WI,CI005008.WI,CI005009.WI,CI005010.WI,CI005011.WI,CI005012.WI,CI005013.WI,CI005014.WI,CI005015.WI,CI005016.WI,CI005017.WI,CI005018.WI,CI005019.WI,CI005020.WI,CI005021.WI,CI005022.WI,CI005023.WI,CI005024.WI,CI005025.WI,CI005026.WI,CI005027.WI,CI005028.WI,CI005029.WI,CI005030.WI,CI005101.WI,CI005102.WI,CI005104.WI,CI005105.WI,CI005106.WI,CI005107.WI,CI005109.WI,CI005110.WI,CI005111.WI,CI005113.WI,CI005117.WI,CI005122.WI,CI005124.WI,CI005127.WI,CI005129.WI,CI005133.WI,CI005134.WI,CI005135.WI,CI005136.WI,CI005137.WI,CI005138.WI,CI005139.WI,CI005140.WI,CI005143.WI,CI005144.WI,CI005145.WI,CI005146.WI,CI005152.WI,CI005153.WI,CI005154.WI,CI005155.WI,CI005156.WI,CI005160.WI,CI005162.WI,CI005163.WI,CI005164.WI,CI005165.WI,CI005166.WI,CI005168.WI,CI005170.WI,CI005171.WI,CI005172.WI,CI005173.WI,CI005178.WI,CI005181.WI,CI005185.WI,CI005187.WI,CI005188.WI,CI005189.WI,CI005190.WI,CI005191.WI,CI005192.WI,CI005193.WI,CI005194.WI,CI005195.WI,CI005196.WI,CI005197.WI,CI005198.WI,CI005199.WI,CI005800.WI,CI005801.WI,CI005802.WI,CI005803.WI,CI005804.WI,CI005805.WI,CI005806.WI,CI005807.WI,CI005808.WI,CI005809.WI,CI005810.WI,CI005811.WI,CI005812.WI,CI005813.WI,CI005814.WI,CI005815.WI,CI005816.WI,CI005817.WI,CI005818.WI,CI005819.WI,CI005820.WI,CI005821.WI,CI005822.WI,CI005823.WI,CI005824.WI,CI005825.WI,CI005826.WI,CI005827.WI,CI005828.WI,CI005829.WI,CI005830.WI,CI005831.WI,CI005832.WI,CI005833.WI,CI005834.WI,CI005835.WI,CI005836.WI,CI005837.WI,CI005838.WI,CI005839.WI,CI005840.WI,CI005841.WI,CI005842.WI,CI005843.WI,CI005844.WI,CI005845.WI,CI005846.WI,CI005847.WI,CI005848.WI,CI005849.WI,CI005201.WI,CI005202.WI,CI005205.WI,CI005206.WI,CI005208.WI,CI005210.WI,CI005211.WI,CI005212.WI,CI005213.WI,CI005214.WI,CI005215.WI,CI005218.WI,CI005220.WI,CI005221.WI,CI005226.WI,CI005227.WI,CI005229.WI,CI005230.WI,CI005231.WI,CI005234.WI,CI005237.WI,CI005238.WI,CI005240.WI,CI005242.WI,CI005247.WI,CI005248.WI,CI005250.WI,CI005252.WI,CI005253.WI,CI005255.WI,CI005259.WI,CI005261.WI,CI005263.WI,CI005267.WI,CI005271.WI,CI005276.WI,CI005277.WI,CI005280.WI,CI005284.WI,CI005286.WI,CI005287.WI,CI005288.WI,CI005289.WI,CI005290.WI,CI005291.WI,CI005292.WI,CI005293.WI,CI005294.WI,CI005295.WI,CI005296.WI,CI005297.WI,CI005299.WI,CI005302.WI,CI005304.WI,CI005305.WI,CI005306.WI,CI005307.WI,CI005309.WI,CI005316.WI,CI005317.WI,CI005318.WI,CI005319.WI,CI005320.WI,CI005321.WI,CI005322.WI,CI005323.WI,CI005324.WI,CI005325.WI,CI005328.WI,CI005330.WI,CI005331.WI,CI005333.WI,CI005337.WI,CI005340.WI,CI005341.WI,CI005342.WI,CI005343.WI,CI005344.WI,CI005345.WI,CI005346.WI,CI005347.WI,CI005349.WI,CI005350.WI,CI005351.WI,CI005353.WI,CI005354.WI,CI005355.WI,CI005357.WI,CI005358.WI,CI005359.WI,CI005360.WI,CI005369.WI,CI005374.WI,CI005381.WI,CI005386.WI,CI005387.WI,CI005388.WI,CI005393.WI,CI005394.WI,CI005396.WI,CI005397.WI,CI005398.WI,CI005399.WI,CI005400.WI,CI005401.WI,CI005402.WI,CI005403.WI,CI005404.WI,CI005405.WI,CI005406.WI,CI005407.WI,CI005408.WI,CI005409.WI,CI005410.WI,CI005411.WI,CI005412.WI,CI005413.WI,CI005414.WI,CI005415.WI,CI005416.WI,CI005417.WI,CI005418.WI,CI005419.WI,CI005420.WI,CI005421.WI,CI005422.WI,CI005423.WI,CI005424.WI,CI005425.WI,CI005426.WI,CI005427.WI,CI005428.WI,CI005429.WI,CI005430.WI,CI005431.WI,CI005432.WI,CI005433.WI,CI005434.WI,CI005435.WI,CI005436.WI,CI005437.WI,CI005438.WI,CI005439.WI,CI005440.WI,CI005441.WI,CI005442.WI,CI005443.WI,CI005444.WI,CI005445.WI,CI005446.WI,CI005447.WI,CI005448.WI,CI005449.WI,CI005450.WI,CI005451.WI,CI005452.WI,CI005453.WI,CI005454.WI,CI005455.WI,CI005456.WI,CI005457.WI,CI005458.WI,CI005459.WI,CI005460.WI,CI005461.WI,CI005462.WI,CI005463.WI,CI005464.WI,CI005465.WI,CI005466.WI,CI005467.WI,CI005468.WI,CI005469.WI,CI005470.WI,CI005471.WI,CI005472.WI,CI005473.WI,CI005474.WI,CI005475.WI,CI005476.WI,CI005477.WI,CI005478.WI,CI005479.WI,CI005480.WI,CI005481.WI,CI005482.WI,CI005483.WI,CI005484.WI,CI005485.WI,CI005486.WI,CI005487.WI,CI005488.WI,CI005489.WI,CI005490.WI,CI005491.WI,CI005492.WI,CI005493.WI,CI005494.WI,CI005495.WI,CI005496.WI,CI005497.WI,CI005498.WI,CI005499.WI,CI005500.WI,CI005501.WI,CI005502.WI,CI005503.WI,CI005504.WI,CI005505.WI,CI005506.WI,CI005507.WI,CI005508.WI,CI005509.WI,CI005510.WI,CI005511.WI,CI005512.WI,CI005513.WI,CI005514.WI,CI005515.WI,CI005516.WI,CI005517.WI,CI005518.WI,CI005519.WI,CI005520.WI,CI005521.WI,CI005522.WI,CI005523.WI,CI005524.WI,CI005525.WI,CI005526.WI,CI005527.WI,CI005528.WI,CI005529.WI,CI005530.WI,CI005531.WI,CI005532.WI,CI005533.WI,CI005534.WI,CI005535.WI,CI005536.WI,CI005537.WI,CI005538.WI,CI005539.WI,CI005540.WI,CI005541.WI,CI005542.WI,CI005543.WI,CI005544.WI,CI005545.WI,CI005546.WI,CI005547.WI,CI005548.WI,CI005549.WI,CI005550.WI,CI005551.WI,CI005552.WI,CI005553.WI,CI005554.WI,CI005555.WI,CI005556.WI,CI005557.WI,CI005558.WI,CI005559.WI,CI005560.WI,CI005561.WI,CI005562.WI,CI005563.WI,CI005564.WI,CI005565.WI,CI005566.WI,CI005567.WI,CI005568.WI,CI005569.WI,CI005570.WI,CI005571.WI,CI005572.WI,CI005573.WI,CI005574.WI,CI005575.WI,CI005576.WI,CI005577.WI,CI005578.WI,CI005579.WI,CI005580.WI,CI005581.WI,CI005917.WI,CI005918.WI,CI005919.WI,CI005920.WI,CI005921.WI,801010.SI,801020.SI,801030.SI,801040.SI,801050.SI,801080.SI,801110.SI,801120.SI,801130.SI,801140.SI,801150.SI,801160.SI,801170.SI,801180.SI,801200.SI,801210.SI,801230.SI,801710.SI,801720.SI,801730.SI,801740.SI,801750.SI,801760.SI,801770.SI,801780.SI,801790.SI,801880.SI,801890.SI,801011.SI,801012.SI,801013.SI,801014.SI,801015.SI,801016.SI,801017.SI,801018.SI,801021.SI,801022.SI,801023.SI,801024.SI,801032.SI,801033.SI,801034.SI,801035.SI,801036.SI,801037.SI,801041.SI,801051.SI,801053.SI,801054.SI,801055.SI,801072.SI,801073.SI,801074.SI,801075.SI,801076.SI,801081.SI,801082.SI,801083.SI,801084.SI,801085.SI,801092.SI,801093.SI,801094.SI,801101.SI,801102.SI,801111.SI,801112.SI,801123.SI,801124.SI,801131.SI,801132.SI,801141.SI,801142.SI,801143.SI,801144.SI,801151.SI,801152.SI,801153.SI,801154.SI,801155.SI,801156.SI,801161.SI,801162.SI,801163.SI,801164.SI,801171.SI,801172.SI,801173.SI,801174.SI,801175.SI,801176.SI,801177.SI,801178.SI,801181.SI,801182.SI,801191.SI,801192.SI,801193.SI,801194.SI,801202.SI,801203.SI,801204.SI,801205.SI,801211.SI,801212.SI,801213.SI,801214.SI,801215.SI,801222.SI,801223.SI,801231.SI,801711.SI,801712.SI,801713.SI,801721.SI,801722.SI,801723.SI,801724.SI,801725.SI,801731.SI,801732.SI,801733.SI,801734.SI,801741.SI,801742.SI,801743.SI,801744.SI,801751.SI,801752.SI,801761.SI,801881.SI,850111.SI,850112.SI,850113.SI,850121.SI,850122.SI,850131.SI,850141.SI,850151.SI,850152.SI,850154.SI,850161.SI,850171.SI,850181.SI,850211.SI,850221.SI,850222.SI,850231.SI,850241.SI,850242.SI,850311.SI,850313.SI,850321.SI,850322.SI,850323.SI,850324.SI,850331.SI,850332.SI,850333.SI,850334.SI,850335.SI,850336.SI,850337.SI,850338.SI,850339.SI,850341.SI,850342.SI,850343.SI,850344.SI,850345.SI,850351.SI,850352.SI,850353.SI,850361.SI,850362.SI,850363.SI,850372.SI,850373.SI,850381.SI,850382.SI,850383.SI,850411.SI,850412.SI,850521.SI,850522.SI,850523.SI,850531.SI,850541.SI,850542.SI,850543.SI,850544.SI,850551.SI,850552.SI,850553.SI,850611.SI,850612.SI,850614.SI,850615.SI,850616.SI,850623.SI,850711.SI,850712.SI,850713.SI,850714.SI,850715.SI,850716.SI,850721.SI,850722.SI,850723.SI,850724.SI,850725.SI,850726.SI,850727.SI,850728.SI,850729.SI,850731.SI,850741.SI,850751.SI,850811.SI,850812.SI,850813.SI,850822.SI,850823.SI,850831.SI,850832.SI,850833.SI,850841.SI,850851.SI,850852.SI,850911.SI,850912.SI,850913.SI,850921.SI,850935.SI,850936.SI,850941.SI,851012.SI,851013.SI,851014.SI,851021.SI,851111.SI,851112.SI,851113.SI,851114.SI,851115.SI,851121.SI,851122.SI,851231.SI,851232.SI,851233.SI,851234.SI,851235.SI,851236.SI,851241.SI,851242.SI,851243.SI,851244.SI,851311.SI,851312.SI,851313.SI,851314.SI,851315.SI,851316.SI,851322.SI,851323.SI,851324.SI,851325.SI,851326.SI,851327.SI,851411.SI,851421.SI,851432.SI,851433.SI,851434.SI,851435.SI,851441.SI,851511.SI,851512.SI,851521.SI,851531.SI,851541.SI,851551.SI,851561.SI,851611.SI,851612.SI,851613.SI,851614.SI,851615.SI,851621.SI,851631.SI,851641.SI,851711.SI,851721.SI,851731.SI,851741.SI,851751.SI,851761.SI,851771.SI,851781.SI,851811.SI,851821.SI,851911.SI,851921.SI,851931.SI,851941.SI,852021.SI,852031.SI,852032.SI,852033.SI,852041.SI,852051.SI,852052.SI,852111.SI,852112.SI,852121.SI,852131.SI,852141.SI,852151.SI,852211.SI,852221.SI,852222.SI,852223.SI,852224.SI,852225.SI,852226.SI,852241.SI,852242.SI,852243.SI,852244.SI,852311.SI,857221.SI,857231.SI,857232.SI,857233.SI,857234.SI,857235.SI,857241.SI,857242.SI,857243.SI,857244.SI,857251.SI,857321.SI,857322.SI,857323.SI,857331.SI,857332.SI,857333.SI,857334.SI,857335.SI,857336.SI,857341.SI,857342.SI,857343.SI,857344.SI,857411.SI,857421.SI,857431.SI,858811.SI,801811.SI,801812.SI,801813.SI,801821.SI,801822.SI,801823.SI,801831.SI,801832.SI,801833.SI,801841.SI,801842.SI,801843.SI,801851.SI,801852.SI,801853.SI,801863.SI,882001.WI,882002.WI,882003.WI,882004.WI,882005.WI,882006.WI,882007.WI,882008.WI,882009.WI,882010.WI,882011.WI,882100.WI,882101.WI,882102.WI,882103.WI,882104.WI,882105.WI,882106.WI,882107.WI,882108.WI,882109.WI,882110.WI,882111.WI,882112.WI,882113.WI,882114.WI,882115.WI,882116.WI,882117.WI,882118.WI,882119.WI,882120.WI,882121.WI,882122.WI,882123.WI,882200.WI,882201.WI,882202.WI,882203.WI,882204.WI,882205.WI,882206.WI,882207.WI,882208.WI,882209.WI,882210.WI,882211.WI,882212.WI,882213.WI,882214.WI,882215.WI,882216.WI,882217.WI,882218.WI,882219.WI,882220.WI,882221.WI,882222.WI,882223.WI,882224.WI,882225.WI,882226.WI,882227.WI,882228.WI,882229.WI,882230.WI,882231.WI,882232.WI,882233.WI,882235.WI,882236.WI,882237.WI,882238.WI,882239.WI,882240.WI,882241.WI,882243.WI,882245.WI,882246.WI,882247.WI,882248.WI,882249.WI,882250.WI,882251.WI,882252.WI,882253.WI,882254.WI,882255.WI,882256.WI,882257.WI,882258.WI,882259.WI,882260.WI,882261.WI,882262.WI,882264.WI,882266.WI,882267.WI,882400.WI,882401.WI,882402.WI,882403.WI,882404.WI,882405.WI,882406.WI,882407.WI,882408.WI,882409.WI,882410.WI,882411.WI,882412.WI,882413.WI,882414.WI,882415.WI,882416.WI,882417.WI,882418.WI,882419.WI,882420.WI,882421.WI,882422.WI,882423.WI,882424.WI,882425.WI,882426.WI,882427.WI,882428.WI,882429.WI,882432.WI,882433.WI,882434.WI,882435.WI,882436.WI,882437.WI,882438.WI,882439.WI,882440.WI,882441.WI,882442.WI,882443.WI,882444.WI,882445.WI,882446.WI,882447.WI,882448.WI,882449.WI,882450.WI,882451.WI,882452.WI,882453.WI,882454.WI,882455.WI,882457.WI,882458.WI,882459.WI,882460.WI,882461.WI,882462.WI,882463.WI,882464.WI,882465.WI,882466.WI,882467.WI,882468.WI,882469.WI,882470.WI,882471.WI,882472.WI,882473.WI,882474.WI,882475.WI,882476.WI,882477.WI,882478.WI,882479.WI,882480.WI,882481.WI,882483.WI,882484.WI,882485.WI,882486.WI,882487.WI,882488.WI,882489.WI,882491.WI,882492.WI,882493.WI,882494.WI,882496.WI,882497.WI,882498.WI,882499.WI,882500.WI,882501.WI,882502.WI,882504.WI,882505.WI,882506.WI,882509.WI,882510.WI,882511.WI,882512.WI,882513.WI,882514.WI,882515.WI,882516.WI,882517.WI,882518.WI,882519.WI,882520.WI,882521.WI,882522.WI,882523.WI,882524.WI,882525.WI,882526.WI,882527.WI,882528.WI,882529.WI,882530.WI,882531.WI,882570.WI,882571.WI,882572.WI,882573.WI,882574.WI,882575.WI,882576.WI,882577.WI,882578.WI,882579.WI,882587.WI,882588.WI,882590.WI,882591.WI,882593.WI,882595.WI,882596.WI,882597.WI,882598.WI,882601.WI,884030.WI,884034.WI,884035.WI,884036.WI,884039.WI,884045.WI,884050.WI,884057.WI,884062.WI,884074.WI,884075.WI,884076.WI,884080.WI,884086.WI,884087.WI,884091.WI,884092.WI,884093.WI,8841000.WI,8841002.WI,8841004.WI,8841007.WI,884101.WI,8841011.WI,8841014.WI,8841018.WI,8841024.WI,884104.WI,8841049.WI,8841050.WI,8841052.WI,8841056.WI,884107.WI,8841070.WI,8841081.WI,8841083.WI,8841087.WI,8841089.WI,8841090.WI,8841096.WI,8841098.WI,8841101.WI,8841107.WI,8841129.WI,8841134.WI,8841136.WI,884114.WI,8841141.WI,8841145.WI,8841149.WI,884116.WI,8841163.WI,8841164.WI,8841165.WI,8841187.WI,8841191.WI,8841222.WI,8841226.WI,8841228.WI,8841230.WI,8841234.WI,8841237.WI,8841240.WI,8841241.WI,8841242.WI,8841244.WI,8841248.WI,8841249.WI,8841255.WI,8841256.WI,8841258.WI,8841259.WI,884126.WI,8841260.WI,8841268.WI,8841272.WI,8841278.WI,8841279.WI,8841280.WI,8841281.WI,8841282.WI,8841284.WI,8841286.WI,8841287.WI,8841288.WI,8841289.WI,884129.WI,8841291.WI,8841294.WI,8841297.WI,8841299.WI,8841300.WI,8841309.WI,884131.WI,8841313.WI,8841314.WI,8841315.WI,8841316.WI,8841318.WI,8841319.WI,884132.WI,8841320.WI,8841321.WI,8841328.WI,884133.WI,8841332.WI,8841337.WI,8841338.WI,8841339.WI,8841344.WI,8841348.WI,8841349.WI,8841350.WI,8841357.WI,8841358.WI,8841360.WI,8841364.WI,8841373.WI,8841375.WI,8841382.WI,8841389.WI,8841392.WI,8841396.WI,8841410.WI,8841411.WI,8841413.WI,8841414.WI,8841415.WI,884156.WI,884157.WI,884159.WI,884160.WI,884161.WI,884162.WI,884166.WI,884169.WI,884173.WI,884178.WI,884181.WI,884184.WI,884185.WI,884186.WI,884189.WI,884190.WI,884195.WI,884197.WI,884201.WI,884202.WI,884207.WI,884208.WI,884211.WI,884214.WI,884215.WI,884216.WI,884224.WI,884228.WI,884232.WI,884239.WI,884242.WI,884243.WI,884246.WI,884249.WI,884250.WI,884251.WI,884252.WI,884253.WI,884254.WI,884662.WI,884677.WI,884685.WI,884701.WI,884705.WI,884782.WI,884785.WI,884800.WI,884816.WI,884871.WI,884876.WI,884878.WI,884880.WI,884894.WI,884895.WI,884953.WI,884963.WI,884969.WI,884987.WI,884995.WI,885040.WI,885041.WI,885042.WI,885020.WI,885021.WI,885022.WI,885023.WI,885024.WI,885025.WI,885026.WI,885027.WI,885028.WI,885029.WI,885030.WI,885031.WI,885032.WI,885033.WI,885034.WI", 
                    "open,high,low,close,volume,amt,pct_chg,swing,vwap,turn",
                    "tradeDate={};priceAdj=U;cycle=D".format(''.join(tradedate.split('-'))))
df_index = pd.DataFrame(index_daily.Data).T
df_index.columns = [x.lower() for x in index_daily.Fields]
df_index.loc[:,'code'] = index_daily.Codes
df_index.loc[:,'date'] = pd.to_datetime(tradedate)

#更新中证500分钟数据
zz500_code = w.wset("sectorconstituent","date={};windcode=000905.SH".format(tradedate))
df_zz500 = pd.DataFrame(zz500_code.Data).T
df_zz500.columns = zz500_code.Fields
code_list = df_zz500.wind_code.unique().tolist()
df_mindata = pd.DataFrame()
for i in range(0, 5):
    min_data = w.wsi(','.join(code_list[i*100:(i+1)*100]), "open,high,low,close,volume,amt,pct_chg", "{} 09:00:00".format(tradedate), "{} 15:00:00".format(tradedate), "") 
    k_df = pd.DataFrame(min_data.Data).T
    k_df.columns = [x.lower() for x in min_data.Fields]
    k_df.loc[:,'datetime'] = min_data.Times
    df_mindata = pd.concat([df_mindata, k_df], axis = 0)    
df_mindata.loc[:,'code'] = df_mindata.windcode
df_mindata.drop(columns = ['windcode'], inplace = True)
df_mindata.reset_index(inplace =True, drop =True)


#更新期权数据
startdate = (pd.to_datetime(tradedate) - timedelta(days = 30)).strftime('%Y-%m-%d')
option_info = w.wset("optioncontractbasicinfo","startdate={};enddate={};exchange=cffex;windcode=000300.SH;status=all".format(startdate, tradedate))
df_option_info = pd.DataFrame(option_info.Data).T
df_option_info.columns = [x.lower() for x in option_info.Fields]
df_option_info.loc[:,'code'] = df_option_info.wind_code
df_option_info.drop(columns = ['wind_code','trade_code'], inplace = True)
df_option_info.loc[:,'date'] = df_option_info.listed_date

option_daily = w.wset("optiondailyquotationstastics","startdate={};enddate={};exchange=cffex;windcode=000300.SH".format(tradedate, tradedate))
df_option = pd.DataFrame(option_daily.Data).T
df_option.columns = [x.lower() for x in option_daily.Fields]
df_option.loc[:,'code'] = df_option.option_code
df_option.drop(columns = ['option_code','tradecode'], inplace = True)
df_option.loc[:,'date'] = pd.to_datetime(tradedate)

if (stock_code.ErrorCode == 0 and 
   stock_daily.ErrorCode == 0 and 
   index_daily.ErrorCode == 0 and 
   zz500_code.ErrorCode == 0 and 
   option_info.ErrorCode == 0 and
   option_daily.ErrorCode == 0):

    df_option.to_csv('{}/k_data/option_daily/日频数据{}.csv'.format(path, tradedate), index = False)
    df_stock.to_csv('{}/k_data/stock_daily/日频数据{}.csv'.format(path, tradedate), index = False)
    df_index.to_csv('{}/k_data/index_daily/日频数据{}.csv'.format(path, tradedate), index = False)
    df_mindata.to_csv('{}/smartmoney/min_k/分钟数据{}.csv'.format(path, tradedate), index = False)
    df_option_info.to_csv('{}/info/option_info/合约信息{}.csv'.format(path, tradedate), index = False)
