from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('login/', views.User_login , name='login'),
    path('logout/',views.User_logout, name='logout'),
    path('exec-profile/',views.Exec_log,name='exec-log'),
    path('about/', views.About , name='about'),
    path('contact/', views.Contact , name='contact'),
    path('tractors/',views.Tractors,name='Tractor'),
    path('implements/', views.Implemns, name='Imps'),
    path('nandi-farming/',views.Nandi_Farming,name='Nandi_Farming'),
    path('dealers-list/',views.Dealer, name='dealer'),
    path('massey-dealers/',views.MasseyDealer, name='masseydealer'),
    path('mahindra-dealers/',views.MahindraDealers, name='mahidealers'),
    path('swaraj-dealers/',views.SwarajDealers, name='sjdealers'),
    path('sonalika-dealers/',views.SonalikaDealers, name='sonalikadealers'),
    path('johndeere-dealers/',views.JDDealers, name='JDdealers'),
    path('force-dealers/',views.ForceDealers, name='forcedealers'),
    path('customer-enrol/',views.Custom, name='customenrol'),
    path('sale-entry/',views.SaleEntry,name='sale'),
    path('ene-sale-check/',views.EneSaleCheck,name='ene-sale-check'),
    path('ene-sale-entry/',views.EneSaleEntry,name='ene-sale'),
    path('non-ene-sale-entry/',views.NonEneSaleEntry,name='non-ene-sale'),
    path('used-trac-verification-entry/',views.UsedTracVerificationEntry,name='used-trac-verify'),
    path('used-trac-status-check/',views.UsedTracStatusCheck,name='used-trac-status-check'),
    path('customer-enrolment-check/',views.CustEneCheck,name='cust-ene-check'),



    
    path('tractors/Mahindra/245-DI-Orchard',views.MD_245DI_ORC,name='245DI_ORC'),
    path('tractors/Mahindra/255-DI-PP',views.MD_255DI_PP,name='255DI_PP'),
    path('tractors/Mahindra/265-DI-PP',views.MD_265DI_PP,name='265DI_PP'),
    path('tractors/Mahindra/265-DI',views.MD_265DI,name='265DI'),
    path('tractors/Mahindra/275-DI-ECO',views.MD_275DI_ECO,name='275DI_ECO'),
    path('tractors/Mahindra/275DI-TU',views.MD_275DI_TU,name='275DI_TU'),
    path('tractors/Mahindra/275DI-XP-Plus',views.MD_275DI_XP_Plus,name='275DI_XP_PLUS'),
    path('tractors/Mahindra/415-DI',views.MD_415DI,name='415DI'),
    path('tractors/Mahindra/475DI-SP-Plus',views.MD_475DI_SP,name='475DI_SP_PLUS'),
    path('tractors/Mahindra/475DI-XP-Plus',views.MD_475DI_XP_Plus,name='475DI_XP_PLUS'),
    path('tractors/Mahindra/475-DI',views.MD_475DI,name='475DI'),
    path('tractors/Mahindra/555DI-PP',views.MD_555DI_PP,name='555DI_PP'),
    path('tractors/Mahindra/575DI-XP-Plus',views.MD_575DI_XP_Plus,name='575DI_XP_PLUS'),
    path('tractors/Mahindra/575-DI',views.MD_575DI,name='575DI'),
    path('tractors/Mahindra/585DI-XP-Plus',views.MD_585DI_XP_Plus,name='585DI_XP_PLUS'),
    path('tractors/Mahindra/585-DI',views.MD_585DI,name='585DI'),
    path('tractors/Mahindra/595-DI',views.MD_595DI,name='595DI'),
    path('tractors/Mahindra/Arjun-555DI',views.MD_Arj_555DI,name='ARJ_555DI'),
    path('tractors/Mahindra/Arjun-605-DI-Ultra',views.MD_Arj_605DI_Ultra,name='ARJ_605DI_ULTRA'),
    path('tractors/Mahindra/Arjun-Novo-605-DI-i-4WD',views.MD_Arj_605DI_i_4WD,name='ARJ_NOVO_605DI_i_4WD'),
    path('tractors/Mahindra/Arjun-Novo-605-DI-i-AC',views.MD_Arj_605DI_i_AC,name='ARJ_NOVO_605DI_i_AC'),
    path('tractors/Mahindra/Arjun-Novo-605-DI-MS',views.MD_Arj_605DI_MS,name='ARJ_NOVO_605DI_MS'),
    path('tractors/Mahindra/Arjun-Novo-605-DI-PS',views.MD_Arj_605DI_PS,name='ARJ_NOVO_605DI_PS'),
    path('tractors/Mahindra/JIVO-225-DI',views.MD_JIVO_225DI,name='JIVO_225DI'),
    path('tractors/Mahindra/JIVO-245-DI',views.MD_JIVO_245DI,name='JIVO_245DI'),
    path('tractors/Mahindra/JIVO-365-DI',views.MD_JIVO_365DI,name='JIVO_365DI'),
    path('tractors/Mahindra/NOVO-655-DI',views.MD_NOVO_655DI,name='NOVO_655DI'),
    path('tractors/Mahindra/NOVO-755-DI',views.MD_NOVO_755DI,name='NOVO_755DI'),
    path('tractors/Mahindra/YUVO-265-DI',views.MD_YUVO_265DI,name='YUVO_265DI'),
    path('tractors/Mahindra/YUVO-415-DI',views.MD_YUVO_415DI,name='YUVO_415DI'),
    path('tractors/Mahindra/YUVO-475-DI',views.MD_YUVO_475DI,name='YUVO_475DI'),
    path('tractors/Mahindra/YUVO-575-DI',views.MD_YUVO_575DI,name='YUVO_575DI'),
    path('tractors/Mahindra/YUVO-575-DI-4WD',views.MD_YUVO_575DI_4WD,name='YUVO_575DI_4WD'),
    path('tractors/Mahindra/YUVO-275-DI',views.MD_YUVO_275DI,name='YUVO_275DI'),
    path('tractors/Mahindra/YUVRAJ-215-NXT',views.MD_YUVRAJ_215_NXT,name='YUVRAJ_215_NXT'),


    path('tractors/Force/Abhiman-Mini',views.F_ABHIMAN_MINI,name='ABHIMAN_MINI'),
    path('tractors/Force/Abhiman',views.F_ABHIMAN,name='ABHIMAN'),
    path('tractors/Force/Balwan-400',views.F_BALWAN_400,name='BALWAN_400'),
    path('tractors/Force/Balwan-550',views.F_BALWAN_550,name='BALWAN_550'),
    path('tractors/Force/Orchard-DLX-LT',views.F_ORC_DLX_LT,name='ORC_DLX_LT'),
    path('tractors/Force/Orchard-DLX',views.F_ORC_DLX,name='ORC_DLX'),
    path('tractors/Force/Orchard-Mini',views.F_ORC_MINI,name='ORC_MINI'),
    path('tractors/Force/Sanman-5000',views.F_SANMAN_5000,name='SANMAN_5000'),
    path('tractors/Force/Sanman-6000',views.F_SANMAN_6000,name='SANMAN_6000'),


    path('tractors/Swaraj/Swaraj-717',views.SJ_717,name='717'),
    path('tractors/Swaraj/Swaraj-724-XM-Orchard-NT',views.SJ_724_XM_ORC_NT,name='724_XM_ORC_NT'),
    path('tractors/Swaraj/Swaraj-724-XM',views.SJ_724_XM,name='724_XM'),
    path('tractors/Swaraj/Swaraj-735-FE',views.SJ_735_FE,name='735_FE'),
    path('tractors/Swaraj/Swaraj-735-XM',views.SJ_735_XM,name='735_XM'),
    path('tractors/Swaraj/Swaraj-735-XT',views.SJ_735_XT,name='735_XT'),
    path('tractors/Swaraj/Swaraj-742-FE',views.SJ_742_FE,name='742_FE'),
    path('tractors/Swaraj/Swaraj-742-XT',views.SJ_742_XT,name='742_XT'),
    path('tractors/Swaraj/Swaraj-744-FE-Potato-Expert',views.SJ_744_FE_PE,name='744_FE_PE'),
    path('tractors/Swaraj/Swaraj-744-FE',views.SJ_744_FE,name='744_FE'),
    path('tractors/Swaraj/Swaraj-744-XT',views.SJ_744_XT,name='744_XT'),
    path('tractors/Swaraj/Swaraj-825-XM',views.SJ_825_XM,name='825_XM'),
    path('tractors/Swaraj/Swaraj-834-XM',views.SJ_834_XM,name='834_XM'),
    path('tractors/Swaraj/Swaraj-841-XM',views.SJ_841_XM,name='841_XM'),
    path('tractors/Swaraj/Swaraj-843-XM-OSM',views.SJ_843_XM_OSM,name='843_XM_OSM'),
    path('tractors/Swaraj/Swaraj-843-XM',views.SJ_843_XM,name='843_XM'),
    path('tractors/Swaraj/Swaraj-855-FE',views.SJ_855_FE,name='855_FE'),
    path('tractors/Swaraj/Swaraj-855-XM',views.SJ_855_XM,name='855_XM'),
    path('tractors/Swaraj/Swaraj-960-FE',views.SJ_960_FE,name='960_FE'),
    path('tractors/Swaraj/Swaraj-963-FE',views.SJ_963_FE,name='963_FE'),


    path('tractors/Massey/1030-DI-Mahashakti',views.MF_1030_DI_MS,name='1030_DI_MS'),
    path('tractors/Massey/1035-DI-Dost',views.MF_1035_DI_DOST,name='1035_DI_DOST'),
    path('tractors/Massey/1035-DI-Mahashakti',views.MF_1035_DI_MS,name='1035_DI_MS'),
    path('tractors/Massey/1035-DI-Planetary-Plus',views.MF_1035_DI_PP,name='1035_DI_PP'),
    path('tractors/Massey/1035-DI-Tonner',views.MF_1035_DI_TONNER,name='1035_DI_TONNER'),
    path('tractors/Massey/1035-DI',views.MF_1035_DI,name='1035_DI'),
    path('tractors/Massey/1134-DI',views.MF_1134_DI,name='1134_DI'),
    path('tractors/Massey/241-DI-Dynatech',views.MF_241_DI_DT,name='241_DI_DT'),
    path('tractors/Massey/241-DI-Mahaan',views.MF_241_DI_MAHAAN,name='241_DI_MAHAAN'),
    path('tractors/Massey/241-DI-Planetary-plus',views.MF_241_DI_PP,name='241_DI_PP'),
    path('tractors/Massey/241-DI-Tonner',views.MF_241_DI_TONNER,name='241_DI_TONNER'),
    path('tractors/Massey/241-DI',views.MF_241_DI,name='241_DI'),
    path('tractors/Massey/245-DI',views.MF_245_DI,name='245_DI'),
    path('tractors/Massey/245-Smart',views.MF_245_SMART,name='245_SMART'),
    path('tractors/Massey/2635-4WD',views.MF_2635_4WD,name='2635_4WD'),
    path('tractors/Massey/5245-DI-4WD',views.MF_5245_DI_4WD,name='5245_DI_4WD'),
    path('tractors/Massey/5245-DI-Maha-Mahaan',views.MF_5245_DI_MM,name='5245_DI_MM'),
    path('tractors/Massey/5245-DI-Planetary-Plus',views.MF_5245_DI_PP,name='5245_DI_PP'),
    path('tractors/Massey/6028',views.MF_6028,name='6028'),
    path('tractors/Massey/7250-DI-Power-Up',views.MF_7250_DI_PU,name='7250_DI_PU'),
    path('tractors/Massey/7250-DI',views.MF_7250_DI,name='7250_DI'),
    path('tractors/Massey/9000-Planetary-Plus',views.MF_9000_PP,name='9000_PP'),
    path('tractors/Massey/9500-Smart',views.MF_9500_SMART,name='9500_SMART'),
    path('tractors/Massey/9500-Super-Shuttle-Series',views.MF_9500_SSS,name='9500_SSS'),
    path('tractors/Massey/9500',views.MF_9500,name='9500'),


    path('tractors/JD/3028EN',views.JD_3028EN,name='3028EN'),
    path('tractors/JD/3036E',views.JD_3036E,name='3036E'),
    path('tractors/JD/3036E',views.JD_3036EN,name='3036EN'),
    path('tractors/JD/5005',views.JD_5005,name='5005'),
    path('tractors/JD/5036C',views.JD_5036C,name='5036C'),
    path('tractors/JD/5036D',views.JD_5036D,name='5036D'),
    path('tractors/JD/5038D',views.JD_5038D,name='5038D'),
    path('tractors/JD/5039C',views.JD_5039C,name='5039C'),
    path('tractors/JD/5039D-PowerPro',views.JD_5039D_PP,name='5039D_PP'),
    path('tractors/JD/5039D',views.JD_5039D,name='5039D'),
    path('tractors/JD/5042C',views.JD_5042C,name='5042C'),
    path('tractors/JD/5042D-PowerPro',views.JD_5042D_PP,name='5042D_PP'),
    path('tractors/JD/5042D',views.JD_5042D,name='5042D'),
    path('tractors/JD/5045D-PowerPro',views.JD_5045D_PP,name='5045D_PP'),
    path('tractors/JD/5045D',views.JD_5045D,name='5045D'),
    path('tractors/JD/5050D',views.JD_5050D,name='5050D'),
    path('tractors/JD/5050E',views.JD_5050E,name='5050E'),
    path('tractors/JD/5055E',views.JD_5055E,name='5055E'),
    path('tractors/JD/5060E',views.JD_5060E,name='5060E'),
    path('tractors/JD/5065E',views.JD_5065E,name='5065E'),
    path('tractors/JD/5075E',views.JD_5075E,name='5075E'),
    path('tractors/JD/5105',views.JD_5105,name='5105'),
    path('tractors/JD/5205',views.JD_5205,name='5205'),
    path('tractors/JD/5210-GearPro',views.JD_5210_GP,name='5210_GP'),
    path('tractors/JD/5210',views.JD_5210,name='5210'),
    path('tractors/JD/5305D',views.JD_5305D,name='5305D'),
    path('tractors/JD/5310',views.JD_5310,name='5310'),
    path('tractors/JD/5405-GearPro',views.JD_5405_GP,name='5405_GP'),
    path('tractors/JD/6110B',views.JD_6110B,name='6110B'),
    path('tractors/JD/6120B',views.JD_6120B,name='6120B'),


    path('tractors/Sonalika/Sonalika-Baagban-DI-30',views.SN_BBN_DI_30,name='BBN_DI_30'),
    path('tractors/Sonalika/Sonalika-Baagban-Super-DI-30',views.SN_BBN_SUPER_DI_30,name='BBN_SUPER_DI_30'),
    path('tractors/Sonalika/Sonalika-DI-35-Sikander',views.SN_DI_35_SKD,name='DI_35_SKD'),
    path('tractors/Sonalika/Sonalika-DI-35',views.SN_DI_35,name='DI_35'),
    path('tractors/Sonalika/Sonalika-DI-42-Chatrapathi',views.SN_DI_42_CHTPI,name='DI_42_CHTPI'),
    path('tractors/Sonalika/Sonalika-DI-42-HDM',views.SN_DI_42_HDM,name='DI_42_HDM'),
    path('tractors/Sonalika/Sonalika-DI-42-Rx',views.SN_DI_42_Rx,name='DI_42_Rx'),
    path('tractors/Sonalika/Sonalika-DI-42-Sikander',views.SN_DI_42_SKD,name='DI_42_SKD'),
    path('tractors/Sonalika/Sonalika-DI-47-Rx',views.SN_DI_47_Rx,name='DI_47_Rx'),
    path('tractors/Sonalika/Sonalika-DI-50-Sikander',views.SN_DI_50_SKD,name='DI_50_SKD'),
    path('tractors/Sonalika/Sonalika-DI-52-Rx-Tiger-Series',views.SN_DI_52_Rx_TS,name='DI_52_Rx_TS'),
    path('tractors/Sonalika/Sonalika-DI-60-MM-Super',views.SN_DI_60_MM_SUPER,name='DI_60_MM_SUPER'),
    path('tractors/Sonalika/Sonalika-DI-60-Rx-MM-Super',views.SN_DI_60_Rx_MM_SUPER,name='DI_60_Rx_MM_SUPER'),
    path('tractors/Sonalika/Sonalika-DI-60-Sikander',views.SN_DI_60_SKD,name='DI_60_SKD'),
    path('tractors/Sonalika/Sonalika-DI-60',views.SN_DI_60,name='DI_60'),
    path('tractors/Sonalika/Sonalika-DI-730-II-HDM',views.SN_DI_730_II_HDM,name='DI_730_II_HDM'),
    path('tractors/Sonalika/Sonalika-DI-734',views.SN_DI_734,name='DI_734'),
    path('tractors/Sonalika/Sonalika-DI-740-III',views.SN_DI_740_III,name='DI_740_III'),
    path('tractors/Sonalika/Sonalika-DI-745-III-Chatrapathi',views.SN_DI_745_III_CHTPI,name='DI_745_III_CHTPI'),
    path('tractors/Sonalika/Sonalika-DI-745-III-Sikander',views.SN_DI_745_III_SKD,name='DI_745_III_SKD'),
    path('tractors/Sonalika/Sonalika-DI-750-III-Sikander',views.SN_DI_750_III_SKD,name='DI_750_III_SKD'),
    path('tractors/Sonalika/Sonalika-DI-750-III',views.SN_DI_750_III,name='DI_750_III'),
    path('tractors/Sonalika/Sonalika-GT-20',views.SN_GT_20,name='GT_20'),
    path('tractors/Sonalika/Sonalika-GT-22',views.SN_GT_22,name='GT_22'),
    path('tractors/Sonalika/Sonalika-GT-26',views.SN_GT_26,name='GT_26'),
    path('tractors/Sonalika/Sonalika-GT-28',views.SN_GT_28,name='GT_28'),
    path('tractors/Sonalika/Sonalika-MM-35-DI',views.SN_MM_35_DI,name='MM_35_DI'),
    path('tractors/Sonalika/Sonalika-MM-39-DI',views.SN_MM_39_DI,name='MM_39_DI'),
    path('tractors/Sonalika/Sonalika-MM-41-DI',views.SN_MM_41_DI,name='MM_41_DI'),
    path('tractors/Sonalika/Sonalika-MM-45-DI',views.SN_MM_45_DI,name='MM_45_DI'),
    path('tractors/Sonalika/Sonalika-MM-50-DI',views.SN_MM_50_DI,name='MM_50_DI'),
    path('tractors/Sonalika/Sonalika-Rx-35-Sikander',views.SN_Rx_35_SKD,name='Rx_35_SKD'),
    path('tractors/Sonalika/Sonalika-Rx-35',views.SN_Rx_35,name='Rx_35'),
    path('tractors/Sonalika/Sonalika-Rx-42-Sikander',views.SN_Rx_42_SKD,name='Rx_42_SKD'),
    path('tractors/Sonalika/Sonalika-Rx-47-Sikander',views.SN_Rx_47_SKD,name='Rx_47_SKD'),
    path('tractors/Sonalika/Sonalika-Rx-50-Sikander',views.SN_Rx_50_SKD,name='Rx_50_SKD'),
    path('tractors/Sonalika/Sonalika-Rx-50',views.SN_Rx_50,name='Rx_50'),
    path('tractors/Sonalika/Sonalika-Rx-55-Sikander',views.SN_Rx_55_SKD,name='Rx_55_SKD'),
    path('tractors/Sonalika/Sonalika-Rx-60-Sikander',views.SN_Rx_60_SKD,name='Rx_60_SKD'),
    path('tractors/Sonalika/Sonalika-Rx-60',views.SN_Rx_60,name='Rx_60'),
    path('tractors/Sonalika/Sonalika-Rx-745-III-Sikander',views.SN_Rx_745_III_SKD,name='Rx_745_III_SKD'),
    path('tractors/Sonalika/Sonalika-Rx-745-III',views.SN_Rx_745_III,name='Rx_745_III'),
    path('tractors/Sonalika/Sonalika-Rx-750-III-Sikander',views.SN_Rx_750_III_SKD,name='Rx_750_III_SKD'),
    path('tractors/Sonalika/Sonalika-Worldtrac-60-Rx-Sikander',views.SN_WT_60_Rx_SKD,name='WT_60_Rx_SKD'),
    path('tractors/Sonalika/Sonalika-Worldtrac-60',views.SN_WT_60,name='WT_60'),
    path('tractors/Sonalika/Sonalika-Worldtrac-75',views.SN_WT_75,name='WT_75'),
    path('tractors/Sonalika/Sonalika-Worldtrac-90',views.SN_WT_90,name='WT_90'),




    

]


