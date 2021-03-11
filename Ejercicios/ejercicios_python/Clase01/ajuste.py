# ajuste.py

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/01_Introduccion/03_Numeros.md#ejercicio-111-bonus

# corregí el código anterior de forma que el pago del último mes se ajuste a lo adeudado.
# Asegurate de guardar en el archivo hipoteca.py esta última versión en tu directorio ejercicios_python/Clase01/. Vamos a volver a trabajar con él.

# Ejercicio 1.11


saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
contadorMeses = 0

pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    contadorMeses += 1

    saldo = saldo * (1+tasa/12)

    if saldo <= pago_mensual:
        total_pagado = total_pagado + saldo
        saldo = 0
    elif contadorMeses  >= pago_extra_mes_comienzo and contadorMeses <= pago_extra_mes_fin:
        saldo = saldo - pago_mensual - pago_extra
        total_pagado = total_pagado + pago_mensual + pago_extra  
    else:
        saldo = saldo - pago_mensual
        total_pagado = total_pagado + pago_mensual
    print(contadorMeses, round(total_pagado, 2), round(saldo, 2))

print('Total pagado', round(total_pagado, 2))
print("Meses:", contadorMeses)

## Output:
#
#$ python ajuste.py 
#1 2684.11 499399.22
#2 5368.22 498795.94
#3 8052.33 498190.15
#4 10736.44 497581.83
#5 13420.55 496970.98
#6 16104.66 496357.58
#7 18788.77 495741.63
#8 21472.88 495123.11
#9 24156.99 494502.01
#10 26841.1 493878.33
#11 29525.21 493252.04
#12 32209.32 492623.15
#13 34893.43 491991.64
#14 37577.54 491357.49
#15 40261.65 490720.7
#16 42945.76 490081.26
#17 45629.87 489439.16
#18 48313.98 488794.38
#19 50998.09 488146.91
#20 53682.2 487496.75
#21 56366.31 486843.87
#22 59050.42 486188.28
#23 61734.53 485529.96
#24 64418.64 484868.89
#25 67102.75 484205.06
#26 69786.86 483538.47
#27 72470.97 482869.11
#28 75155.08 482196.95
#29 77839.19 481522.0
#30 80523.3 480844.23
#31 83207.41 480163.64
#32 85891.52 479480.21
#33 88575.63 478793.93
#34 91259.74 478104.8
#35 93943.85 477412.79
#36 96627.96 476717.9
#37 99312.07 476020.11
#38 101996.18 475319.42
#39 104680.29 474615.81
#40 107364.4 473909.27
#41 110048.51 473199.78
#42 112732.62 472487.33
#43 115416.73 471771.92
#44 118100.84 471053.53
#45 120784.95 470332.14
#46 123469.06 469607.75
#47 126153.17 468880.34
#48 128837.28 468149.89
#49 131521.39 467416.41
#50 134205.5 466679.87
#51 136889.61 465940.26
#52 139573.72 465197.56
#53 142257.83 464451.78
#54 144941.94 463702.88
#55 147626.05 462950.87
#56 150310.16 462195.72
#57 152994.27 461437.43
#58 155678.38 460675.97
#59 158362.49 459911.34
#60 161046.6 459143.53
#61 164730.71 457372.52
#62 168414.82 455594.13
#63 172098.93 453808.33
#64 175783.04 452015.09
#65 179467.15 450214.37
#66 183151.26 448406.16
#67 186835.37 446590.4
#68 190519.48 444767.09
#69 194203.59 442936.17
#70 197887.7 441097.63
#71 201571.81 439251.43
#72 205255.92 437397.53
#73 208940.03 435535.91
#74 212624.14 433666.54
#75 216308.25 431789.37
#76 219992.36 429904.38
#77 223676.47 428011.54
#78 227360.58 426110.81
#79 231044.69 424202.16
#80 234728.8 422285.56
#81 238412.91 420360.97
#82 242097.02 418428.37
#83 245781.13 416487.71
#84 249465.24 414538.97
#85 253149.35 412582.1
#86 256833.46 410617.08
#87 260517.57 408643.88
#88 264201.68 406662.45
#89 267885.79 404672.77
#90 271569.9 402674.79
#91 275254.01 400668.5
#92 278938.12 398653.84
#93 282622.23 396630.79
#94 286306.34 394599.3
#95 289990.45 392559.36
#96 293674.56 390510.91
#97 297358.67 388453.93
#98 301042.78 386388.38
#99 304726.89 384314.22
#100 308411.0 382231.42
#101 312095.11 380139.94
#102 315779.22 378039.75
#103 319463.33 375930.8
#104 323147.44 373813.07
#105 326831.55 371686.52
#106 330515.66 369551.1
#107 334199.77 367406.79
#108 337883.88 365253.54
#109 340567.99 364091.32
#110 343252.1 362924.25
#111 345936.21 361752.33
#112 348620.32 360575.52
#113 351304.43 359393.81
#114 353988.54 358207.17
#115 356672.65 357015.59
#116 359356.76 355819.05
#117 362040.87 354617.52
#118 364724.98 353410.98
#119 367409.09 352199.41
#120 370093.2 350982.8
#121 372777.31 349761.12
#122 375461.42 348534.35
#123 378145.53 347302.47
#124 380829.64 346065.45
#125 383513.75 344823.28
#126 386197.86 343575.93
#127 388881.97 342323.39
#128 391566.08 341065.63
#129 394250.19 339802.62
#130 396934.3 338534.36
#131 399618.41 337260.81
#132 402302.52 335981.95
#133 404986.63 334697.76
#134 407670.74 333408.23
#135 410354.85 332113.32
#136 413038.96 330813.02
#137 415723.07 329507.29
#138 418407.18 328196.13
#139 421091.29 326879.5
#140 423775.4 325557.39
#141 426459.51 324229.77
#142 429143.62 322896.62
#143 431827.73 321557.91
#144 434511.84 320213.63
#145 437195.95 318863.74
#146 439880.06 317508.23
#147 442564.17 316147.07
#148 445248.28 314780.24
#149 447932.39 313407.71
#150 450616.5 312029.47
#151 453300.61 310645.48
#152 455984.72 309255.73
#153 458668.83 307860.18
#154 461352.94 306458.82
#155 464037.05 305051.62
#156 466721.16 303638.56
#157 469405.27 302219.61
#158 472089.38 300794.75
#159 474773.49 299363.95
#160 477457.6 297927.19
#161 480141.71 296484.45
#162 482825.82 295035.69
#163 485509.93 293580.89
#164 488194.04 292120.04
#165 490878.15 290653.09
#166 493562.26 289180.04
#167 496246.37 287700.85
#168 498930.48 286215.49
#169 501614.59 284723.94
#170 504298.7 283226.18
#171 506982.81 281722.18
#172 509666.92 280211.92
#173 512351.03 278695.36
#174 515035.14 277172.48
#175 517719.25 275643.25
#176 520403.36 274107.65
#177 523087.47 272565.66
#178 525771.58 271017.24
#179 528455.69 269462.37
#180 531139.8 267901.02
#181 533823.91 266333.16
#182 536508.02 264758.77
#183 539192.13 263177.83
#184 541876.24 261590.29
#185 544560.35 259996.14
#186 547244.46 258395.35
#187 549928.57 256787.88
#188 552612.68 255173.72
#189 555296.79 253552.84
#190 557980.9 251925.2
#191 560665.01 250290.78
#192 563349.12 248649.54
#193 566033.23 247001.47
#194 568717.34 245346.54
#195 571401.45 243684.7
#196 574085.56 242015.95
#197 576769.67 240340.24
#198 579453.78 238657.54
#199 582137.89 236967.84
#200 584822.0 235271.1
#201 587506.11 233567.28
#202 590190.22 231856.37
#203 592874.33 230138.33
#204 595558.44 228413.13
#205 598242.55 226680.74
#206 600926.66 224941.13
#207 603610.77 223194.28
#208 606294.88 221440.14
#209 608978.99 219678.7
#210 611663.1 217909.92
#211 614347.21 216133.77
#212 617031.32 214350.21
#213 619715.43 212559.23
#214 622399.54 210760.78
#215 625083.65 208954.84
#216 627767.76 207141.38
#217 630451.87 205320.36
#218 633135.98 203491.75
#219 635820.09 201655.52
#220 638504.2 199811.64
#221 641188.31 197960.08
#222 643872.42 196100.8
#223 646556.53 194233.78
#224 649240.64 192358.98
#225 651924.75 190476.36
#226 654608.86 188585.91
#227 657292.97 186687.57
#228 659977.08 184781.33
#229 662661.19 182867.14
#230 665345.3 180944.97
#231 668029.41 179014.8
#232 670713.52 177076.59
#233 673397.63 175130.3
#234 676081.74 173175.9
#235 678765.85 171213.35
#236 681449.96 169242.63
#237 684134.07 167263.7
#238 686818.18 165276.52
#239 689502.29 163281.06
#240 692186.4 161277.29
#241 694870.51 159265.17
#242 697554.62 157244.66
#243 700238.73 155215.74
#244 702922.84 153178.36
#245 705606.95 151132.5
#246 708291.06 149078.1
#247 710975.17 147015.15
#248 713659.28 144943.61
#249 716343.39 142863.43
#250 719027.5 140774.58
#251 721711.61 138677.03
#252 724395.72 136570.74
#253 727079.83 134455.68
#254 729763.94 132331.8
#255 732448.05 130199.07
#256 735132.16 128057.46
#257 737816.27 125906.92
#258 740500.38 123747.42
#259 743184.49 121578.93
#260 745868.6 119401.4
#261 748552.71 117214.79
#262 751236.82 115019.08
#263 753920.93 112814.21
#264 756605.04 110600.16
#265 759289.15 108376.89
#266 761973.26 106144.35
#267 764657.37 103902.51
#268 767341.48 101651.32
#269 770025.59 99390.76
#270 772709.7 97120.78
#271 775393.81 94841.34
#272 778077.92 92552.4
#273 780762.03 90253.93
#274 783446.14 87945.87
#275 786130.25 85628.2
#276 788814.36 83300.88
#277 791498.47 80963.86
#278 794182.58 78617.09
#279 796866.69 76260.56
#280 799550.8 73894.2
#281 802234.91 71517.98
#282 804919.02 69131.86
#283 807603.13 66735.8
#284 810287.24 64329.76
#285 812971.35 61913.69
#286 815655.46 59487.55
#287 818339.57 57051.31
#288 821023.68 54604.91
#289 823707.79 52148.32
#290 826391.9 49681.5
#291 829076.01 47204.39
#292 831760.12 44716.97
#293 834444.23 42219.18
#294 837128.34 39710.98
#295 839812.45 37192.33
#296 842496.56 34663.19
#297 845180.67 32123.51
#298 847864.78 29573.25
#299 850548.89 27012.36
#300 853233.0 24440.8
#301 855917.11 21858.53
#302 858601.22 19265.5
#303 861285.33 16661.66
#304 863969.44 14046.97
#305 866653.55 11421.39
#306 869337.66 8784.87
#307 872021.77 6137.36
#308 874705.88 3478.83
#309 877389.99 809.21
#310 878202.57 0
#Total pagado 878202.57
#Meses: 310