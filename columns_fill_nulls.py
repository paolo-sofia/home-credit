import polars as pl

UNKNOWN_COLUMNS: list[str] = [
    "conts_type_509L",
    "incometype_1044T",
    "empl_industry_691L",
    "credtype_587L",
    "inittransactioncode_279L",
    "status_219L",
    "rejectreason_755M",
    "cancelreason_3545846M",
    "rejectreasonclient_4145042M",
    "lastst_736L",
    "role_1084L",
    "disbursementtype_67L",
    "twobodfilling_608L",
    "credtype_322L",
    "inittransactioncode_186L",
    "typesuite_864L",
    "bankacctype_710L",
    "paytype1st_925L",
    "credacc_status_367L",
]

NO_DEDUCTION_COLUMNS: list[str] = ["requesttype_4525192L"]

FILL_ONE_COLUMNS: list[str] = ["firstclxcampaign_1125D"]

A55475B1_COLUMNS: list[str] = [
    "postype_4733339M",
    "profession_152M",
    "conts_role_79M",
    "empls_economicalst_849M",
    "cacccardblochreas_147M",
    "description_5085714M",
    "education_1103M",
    "education_88M",
    "maritalst_385M",
    "maritalst_893M",
]

FILL_ZERO_COLUMNS: list[str] = [
    "byoccupationinc_3656910L",
    "credacc_transactions_402L",
    "amtdebitincoming_4809443A",
    "amtdebitoutgoing_4809440A",
    "amtdepositbalance_4809441A",
    "amtdepositincoming_4809444A",
    "amtdepositoutgoing_4809442A",
    "credacc_actualbalance_314A",
    "credacc_maxhisbal_375A",
    "credacc_minhisbal_90A",
    "amount_416A",
    "revolvingaccount_394A",
    "mainoccupationinc_384A",
    "annuity_853A",
    "credamount_590A",
    "downpmt_134A",
    "credacc_credlmt_575A",
    "actualdpd_943P",
    "pmtscount_423L",
    "pmtssum_45A",
    "maxpmtlast3m_4525190A",
    "numinstmatpaidtearly2d_4499204L",
    "numinstpaid_4499208L",
    "numinstpaidearly5dobd_4499205L",
    "numinstpaidearly3dest_4493216L",
    "numinstpaidearly5dest_4493211L",
    "numinstpaidearlyest_4493214L",
    "numinstregularpaidest_4493210L",
    "numinsttopaygrest_4493213L",
    "numinstunpaidmaxest_4493212L",
    "sumoutstandtotalest_4493215A",
    "maxdpdinstlnum_3546846P",
    "lastrejectcredamount_222A",
    "avgmaxdpdlast9m_3716943P",
    "maxdpdtolerance_577P",
    "maxdpdtolerance_577P",
    "maxdbddpdtollast12m_3658940P",
    "approvaldate_319D",
    "approvaldate_319D",
    "outstandingdebt_522A",
    "outstandingdebt_522A",
    "currdebt_94A",
    "currdebt_94A",
    "numinstpaidlastcontr_4325080L",
    "avginstallast24m_3658937A",
    "maxoutstandbalancel12m_4187113A",
    "maxinstallast24m_3658928A",
    "avgdbddpdlast24m_3658932P",
    "mindbddpdlast24m_3658935P",
    "numinstlswithdpd5_4187116L",
    "maininc_215A",
    "avgdpdtolclosure24_3658938P",
    "pctinstlsallpaidlat10d_839L",
    "cntpmts24_3658933L",
    "pctinstlsallpaidlate6d_3546844L",
    "pctinstlsallpaidlate4d_3546849L",
    "pctinstlsallpaidearl3d_427L",
    "pctinstlsallpaidlate1d_3546856L",
    "numinstlswithdpd10_728L",
    "numinstlswithoutdpd_562L",
    "numinstregularpaid_973L",
    "cntincpaycont9m_3716944L",
    "numincomingpmts_3546848L",
    "lastactivateddate_801D",
    "daysoverduetolerancedd_3976961L",
    "numinsttopaygr_769L",
    "numinstunpaidmax_3546851L",
    "monthsannuity_845L",
    "numinstpaidearly5d_1087L",
    "numinstpaidearly_338L",
    "numinstpaidlate1d_3546852L",
    "numinstpaidearly3d_3546850L",
    "numinstlallpaidearly3d_817L",
    "numinstlsallpaid_934L",
    "lastapprcredamount_781A",
    "sumoutstandtotal_3546847A",
    "actualdpdtolerance_344P",
    "pmtnum_8L",
    "pmtnum_8L",
    "tenor_203L",
    "tenor_203L",
    "commnoinclast6m_3546845L",
    "maxdpdfrom6mto36m_3546853P",
    "maxdpdfrom6mto36m_3546853P",
    "mainoccupationinc_437A",
    "mainoccupationinc_437A",
    "maxannuity_159A",
    "maxdebt4_972A",
    "maxdpdlast12m_727P",
    "maxdpdlast24m_143P",
    "maxdpdlast3m_392P",
    "maxdpdlast6m_474P",
    "maxdpdlast9m_1059P",
    "maxdpdtolerance_374P",
    "opencred_647L",
    "price_1097A",
    "days120_123L",
    "days180_256L",
    "days30_165L",
    "days360_512L",
    "days90_310L",
    "firstquarter_103L",
    "fourthquarter_440L",
    "numberofqueries_373L",
    "secondquarter_766L",
    "thirdquarter_1082L",
    "pmtnum_254L",
    "annuitynextmonth",
    "currdebt_22A",
    "currdebtcredtyperange_828A",
    "numinstls_657L",
    "totalsettled_863A",
    "totaldebt_9A",
    "avgoutstandbalancel6m_4187114A",
    "annuitynextmonth_57A",
]

FILL_MINUS_ONE_COLUMNS: list[str] = [
    "eir_270L",
    "interestrate_311L",
    "totinstallast1m_4525188A",
    "maxlnamtstart6m_4525199A",
    "avgpmtlast12m_4525200A",
    "amtinstpaidbefduel24m_4187115A",
    "mastercontrelectronic_519L",
    "mastercontrexist_109L",
    "isdebitcard_527L",
    "isbidproduct_390L",
]

INDICATOR_COLUMNS: list[str] = [
    "posfpd30lastmonth_3976960P",
    "empls_employedfrom_796D",
    "posfpd10lastmonth_333P",
    "lastdelinqdate_224D",
    "dtlastpmtallstes_4499206D",
    "avgdbdtollast24m_4525197P",
    "mindbdtollast24m_4525191P",
    "maxdbddpdlast1m_3658939P",
    "empl_employedfrom_271D",
    "employedfrom_700D",
    "avgdbddpdlast3m_4187120P",
    "datelastunpaid_3546854D",
    "maxdbddpdtollast6m_4187119P",
    "responsedate_4527233D",
    "lastrejectdate_50D",
    "datefirstoffer_1144D",
    "maxdpdinstldate_3546855D",
    "responsedate_1012D",
    "dtlastpmtallstes_3545839D",
    "dateactivated_425D",
    "maxdbddpdtollast12m_3658940P",
    "lastapplicationdate_877D",
    "posfstqpd30lastmonth_3976962P",
    "creationdate_885D",
    "firstdatedue_489D",
    "firstnonzeroinstldate_307D",
    "lastapprdate_640D",
    "contractenddate_991D",
    "openingdate_313D",
    "dtlastpmt_581D",
    "birth_259D",
]

NULL_COLUMNS = ["paytype1st_925L", "paytype_783L"]

ALL_COLUMNS = (
    FILL_MINUS_ONE_COLUMNS
    + FILL_ONE_COLUMNS
    + FILL_ZERO_COLUMNS
    + INDICATOR_COLUMNS
    + A55475B1_COLUMNS
    + UNKNOWN_COLUMNS
    + NO_DEDUCTION_COLUMNS
    + NULL_COLUMNS
)


def fill_nulls(data: pl.LazyFrame) -> pl.LazyFrame:
    data = data.with_columns(
        *[
            pl.when(pl.col(col).is_null()).then(pl.lit(1)).otherwise(pl.lit(0)).alias(col)
            for col in set(data.columns).intersection(INDICATOR_COLUMNS)
        ]
    )

    data = data.with_columns(
        *[pl.col(col).fill_null("UNKNOWN") for col in set(data.columns).intersection(UNKNOWN_COLUMNS)]
    )

    data = data.with_columns(
        *[pl.col(col).fill_null("a55475b1") for col in set(data.columns).intersection(A55475B1_COLUMNS)]
    )

    data = data.with_columns(
        *[pl.col(col).fill_null("NO_DEDUCTION") for col in set(data.columns).intersection(NO_DEDUCTION_COLUMNS)]
    )

    data = data.with_columns(*[pl.col(col).fill_null("NULL") for col in set(data.columns).intersection(NULL_COLUMNS)])

    data = data.with_columns(
        *[pl.col(col).fill_null(-1.0) for col in set(data.columns).intersection(FILL_MINUS_ONE_COLUMNS)]
    )

    data = data.with_columns(*[pl.col(col).fill_null(0.0) for col in set(data.columns).intersection(FILL_ZERO_COLUMNS)])

    return data.with_columns(*[pl.col(col).fill_null(1.0) for col in set(data.columns).intersection(FILL_ONE_COLUMNS)])
