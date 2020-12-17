# Analysis of the German football transfer market
Using data from transfermarkt.de to predict transfer values and alayze the transfer market
![](./assets/expenditure_over_time.png)

Example output:
'''html
<!DOCTYPE html>
<html class="no-js" lang="de"> <!--<![endif]-->
<head>



<script src='https://www.asadcdn.com/adlib/pages/transfermarkt.js'></script>
    <meta charset="utf-8"/>
    <meta http-equiv="x-ua-compatible" content="IE=edge">
    <meta name="format-detection" content="telephone=no">
    <meta name="theme-color" content="#1a3151"/>
	    <link rel="shortcut icon" href="/favicon.ico" type="image/x-icon"/>
    <link rel="shortcut icon" sizes="16x16" href="/favicon-16x16.png">
    <link rel="shortcut icon" sizes="192x192" href="/android-chrome-192x192.png">
    <link rel="apple-touch-icon-precomposed" href="/apple-touch-icon-152x152.png">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=2.0, user-scalable=no" />
<meta name="keywords" content="1. Bundesliga,Deutschland" />
<meta name="description" content="Die Statistik zeigt die Transferübersicht der 1. Bundesliga aus der Saison 19/20. Die Klubs werden nach ihren Platzierungen der Vorsaison absteigend dargestellt." />
<meta property="og:type" content="article" />
<meta property="og:image" content="https://tmssl.akamaized.net/images/tm_logo.png" />
<meta property="og:description" content="" />
<meta property="og:title" content="1. Bundesliga - Transfers 19/20" />
<meta property="og:url" content="https://_/1-bundesliga/transfers/wettbewerb/L1/plus/?saison_id=2019&amp;s_w=s&amp;leihe=0&amp;intern=0" />
<link hreflang="de" rel="alternate" href="https://www.transfermarkt.de/1-bundesliga/transfers/wettbewerb/L1/saison_id/2019/s_w/s/leihe/0/intern/0/plus/" />
<link rel="stylesheet" type="text/css" href="https://tmssl.akamaized.net/css/stylesheets/menue.css?lm=1605863819" />
<link rel="stylesheet" type="text/css" href="https://tmssl.akamaized.net/css/stylesheets/tm-grid.css?lm=1605863819" />
<link rel="stylesheet" type="text/css" href="https://tmssl.akamaized.net/css/stylesheets/main.css?lm=1605863819" />
<link rel="stylesheet" type="text/css" href="https://tmssl.akamaized.net/css/foundation-icons.css?lm=1605863819" />
<link rel="stylesheet" type="text/css" href="https://tmssl.akamaized.net/assets/b7c5571cf8957553f95f6d9069eaed67/jui/css/base/jquery-ui.css?lm=1605863833" />
<link rel="stylesheet" type="text/css" href="https://tmssl.akamaized.net/css/stylesheets/main_desktop.css?lm=1605863819" />
<link rel="stylesheet" type="text/css" href="https://tmssl.akamaized.net/css/sprite-main.css?lm=1605863819" />
<link rel="stylesheet" type="text/css" href="https://tmssl.akamaized.net/css/chosen.css?lm=1605863819" />
<link rel="stylesheet" type="text/css" href="https://tmssl.akamaized.net/css/jquery-ui-1.10.4.custom.css?lm=1605863819" />
<link rel="stylesheet" type="text/css" href="https://tmssl.akamaized.net/css/jquery-ui-1.10.4.tm-theme.css?lm=1605863819" />
<link rel="stylesheet" type="text/css" href="https://tmssl.akamaized.net/css/stylesheets/main_werbung.css?lm=1605863819" />
<link rel="stylesheet" type="text/css" href="https://tmssl.akamaized.net/css/shortclasses.css?lm=1605863819" />
<link rel="stylesheet" type="text/css" href="https://tmssl.akamaized.net/css/print.css?_sn=1?lm=1605863819" media="print" />
<link rel="stylesheet" type="text/css" href="https://tmssl.akamaized.net/css/wettbewerb.css?lm=1605863819" />
<link rel="stylesheet" type="text/css" href="https://tmssl.akamaized.net/css/statistiken.css?lm=1605863819" />
<link rel="stylesheet" type="text/css" href="https://tmssl.akamaized.net/css/desktop.css?lm=1605863819" />
<link rel="stylesheet" type="text/css" href="https://tmssl.akamaized.net/css/domainspezifisch/desktop-de.css?lm=1605863819" />
<link rel="stylesheet" type="text/css" href="https://tmssl.akamaized.net/assets/bdb39bc7538f732f9833170435d23c28/css/tooltipster.css?lm=1605863833" />
<title>1. Bundesliga - Transfers 19/20 | Transfermarkt</title>
                <script type="module" src="https://tmsi.akamaized.net/js/globals/tm-global-elements.esm.js?v=4"></script>
            <script nomodule="" src="https://tmsi.akamaized.net/js/globals/tm-global-elements.js?v=4"></script>
</script>
    <style>
        @font-face {
            font-family: 'OSL';
            font-style: normal;
            font-weight: normal;
            src: local('Open Sans Cond Light'), local('OpenSans-CondensedLight'),
            url(https://tmsi.akamaized.net/fonts/OpenSans-CondensedLight.woff) format('woff');
        }

        @font-face {
            font-family: 'OSB';
            font-style: normal;
            font-weight: normal;
            src: local('Open Sans Cond Light'), local('OpenSans-CondensedLight'),
            url(https://tmsi.akamaized.net/fonts/OpenSans-CondensedLight.woff) format('woff');
        }

        @font-face {
            font-family: 'Source Sans Pro';
            font-style: normal;
            font-weight: normal;
            src: local('Source Sans Pro'), local('SourceSansPro-Regular'),
            url(https://tmsi.akamaized.net/fonts/SourceSansPro-Regular.woff) format('woff');
        }

        @font-face {
            font-family: 'Source Sans Pro';
            font-style: normal;
            font-weight: bold;
            src: local('Source Sans Pro Bold'), local('SourceSansPro-Bold'),
            url(https://tmsi.akamaized.net/fonts/SourceSansPro-Bold.woff) format('woff');
        }

        @font-face {
            font-family: 'Oswald';
            font-style: normal;
            font-weight: lighter;
            src: url(https://tmsi.akamaized.net/fonts/oswald_light.woff) format('woff');
        }

        @font-face {
            font-family: 'Oswald';
            font-style: normal;
            font-weight: normal;
            src: url(https://tmsi.akamaized.net/fonts/oswald_regular.woff) format('woff');
        }

        @font-face {
            font-family: 'Oswald';
            font-style: normal;
            font-weight: bold;
            src: url(https://tmsi.akamaized.net/fonts/oswald_bold.woff) format('woff');
        }

        @font-face {
            font-family: "socicon";
            src: url("https://tmsi.akamaized.net/fonts/socicon.eot");
            src: url("https://tmsi.akamaized.net/fonts/socicon.eot?#iefix") format("embedded-opentype"),
            url("https://tmsi.akamaized.net/fonts/socicon.woff") format("woff"),
            url("https://tmsi.akamaized.net/fonts/socicon.ttf") format("truetype"),
            url("https://tmsi.akamaized.net/fonts/socicon.svg#socicon") format("svg");
            font-weight: normal;
            font-style: normal;
        }
    </style>
    
</head>
<body x-ms-format-detection="none" style="overflow-y: scroll;"
      class="" itemscope
      itemtype="http://schema.org/WebPage">

<div id="main">
<div class="row">
	<div class="large-12 columns">
			<div class="box">

			<div class="box">
			<div class="table-header" id="to-86"><a class="vereinprofil_tooltip" id="86" href="/sv-werder-bremen/transfers/verein/86/saison_id/2019"><img src="https://tmssl.akamaized.net/images/wappen/small/86.png?lm=1403082298" title="&nbsp;" alt="SV Werder Bremen" class="" /></a><h2><a class="vereinprofil_tooltip" id="86" href="/sv-werder-bremen/transfers/verein/86/saison_id/2019">SV Werder Bremen</a></h2></div>
			<div class="responsive-table">
				<table>
					<thead>
						<tr>
							<th class="spieler-transfer-cell">Zugang</th>
							<th class="zentriert alter-transfer-cell">Alter</th>
							<th class="zentriert nat-transfer-cell">Nat.</th>
							<th class="pos-transfer-cell">Position</th>
							<th class="kurzpos-transfer-cell zentriert">Pos</th>
							<th class="rechts mw-transfer-cell">Marktwert</th>
							<th colspan="2" class="verein-transfer-cell">Abgebender Verein</th>
							<th class="rechts abloese-transfer-cell">Ablöse</th>
							<th class="rechts abloese-transfer-cell">Prediction</th>
						</tr>
					</thead>
					<tbody>
															<tr>
									<td><div class="di nowrap"><span class="hide-for-small"><a title="Niclas Füllkrug" class="spielprofil_tooltip" id="75489" href="/niclas-fullkrug/profil/spieler/75489">Niclas Füllkrug</a></span></div><div class="di nowrap"><span class="show-for-small"><a title="Niclas Füllkrug" class="spielprofil_tooltip" id="75489" href="/niclas-fullkrug/profil/spieler/75489">N. Füllkrug</a></span></div></td>
									<td class="zentriert alter-transfer-cell">26</td>
									<td class="zentriert nat-transfer-cell"><img src="https://tmssl.akamaized.net/images/flagge/tiny/40.png?lm=1520612525" title="Deutschland" alt="Deutschland" class="flaggenrahmen" /></td>
									<td class="pos-transfer-cell">Mittelstürmer</td>
									<td class="kurzpos-transfer-cell zentriert">MS</td>
									<td class="rechts mw-transfer-cell">8,00 Mio. €</td>
									<td class="no-border-rechts zentriert"><a class="vereinprofil_tooltip" id="42" href="/hannover-96/transfers/verein/42/saison_id/2019"><img src="https://tmssl.akamaized.net/images/wappen/tiny/42.png?lm=1396275305" title="&nbsp;" alt="Hannover 96" class="tiny_wappen" /></a></td>
									<td class="no-border-links verein-flagge-transfer-cell"> <img src="https://tmssl.akamaized.net/images/flagge/tiny/40.png?lm=1520612525" title="Deutschland" alt="Deutschland" class="flaggenrahmen" />&nbsp;&nbsp;<a class="vereinprofil_tooltip" id="42" href="/hannover-96/transfers/verein/42/saison_id/2019">Hannover 96</a></td>
									<td class="rechts "><a href="/jumplist/transfers/spieler/75489/transfer_id/2460580">6,50 Mio. €</a></td>
									<td class="rechts "><b>7,53 Mio. €</b></td>
								</tr>
										<tr>
									<td><div class="di nowrap"><span class="hide-for-small"><a title="Marco Friedl" class="spielprofil_tooltip" id="156990" href="/marco-friedl/profil/spieler/156990">Marco Friedl</a></span></div><div class="di nowrap"><span class="show-for-small"><a title="Marco Friedl" class="spielprofil_tooltip" id="156990" href="/marco-friedl/profil/spieler/156990">M. Friedl</a></span></div></td>
									<td class="zentriert alter-transfer-cell">21</td>
									<td class="zentriert nat-transfer-cell"><img src="https://tmssl.akamaized.net/images/flagge/tiny/127.png?lm=1520611569" title="Österreich" alt="Österreich" class="flaggenrahmen" /></td>
									<td class="pos-transfer-cell">Innenverteidiger</td>
									<td class="kurzpos-transfer-cell zentriert">IV</td>
									<td class="rechts mw-transfer-cell">2,50 Mio. €</td>
									<td class="no-border-rechts zentriert"><a class="vereinprofil_tooltip" id="27" href="/fc-bayern-munchen/transfers/verein/27/saison_id/2019"><img src="https://tmssl.akamaized.net/images/wappen/tiny/27.png?lm=1498251238" title="&nbsp;" alt="FC Bayern München" class="tiny_wappen" /></a></td>
									<td class="no-border-links verein-flagge-transfer-cell"> <img src="https://tmssl.akamaized.net/images/flagge/tiny/40.png?lm=1520612525" title="Deutschland" alt="Deutschland" class="flaggenrahmen" />&nbsp;&nbsp;<a class="vereinprofil_tooltip" id="27" href="/fc-bayern-munchen/transfers/verein/27/saison_id/2019">Bayern München</a></td>
									<td class="rechts "><a href="/jumplist/transfers/spieler/156990/transfer_id/2488867">3,50 Mio. €</a></td>
									<td class="rechts "><b>3.51 Mio. €</b></td>
								</tr>
										<tr>
									<td><div class="di nowrap"><span class="hide-for-small"><a title="Benjamin Goller" class="spielprofil_tooltip" id="388058" href="/benjamin-goller/profil/spieler/388058">Benjamin Goller</a></span></div><div class="di nowrap"><span class="show-for-small"><a title="Benjamin Goller" class="spielprofil_tooltip" id="388058" href="/benjamin-goller/profil/spieler/388058">B. Goller</a></span></div></td>
									<td class="zentriert alter-transfer-cell">20</td>
									<td class="zentriert nat-transfer-cell"><img src="https://tmssl.akamaized.net/images/flagge/tiny/40.png?lm=1520612525" title="Deutschland" alt="Deutschland" class="flaggenrahmen" /></td>
									<td class="pos-transfer-cell">Rechtsaußen</td>
									<td class="kurzpos-transfer-cell zentriert">RA</td>
									<td class="rechts mw-transfer-cell">400 Tsd. €</td>
									<td class="no-border-rechts zentriert"><a class="vereinprofil_tooltip" id="33" href="/fc-schalke-04/transfers/verein/33/saison_id/2019"><img src="https://tmssl.akamaized.net/images/wappen/tiny/33.png?lm=1433588238" title="&nbsp;" alt="FC Schalke 04" class="tiny_wappen" /></a></td>
									<td class="no-border-links verein-flagge-transfer-cell"> <img src="https://tmssl.akamaized.net/images/flagge/tiny/40.png?lm=1520612525" title="Deutschland" alt="Deutschland" class="flaggenrahmen" />&nbsp;&nbsp;<a class="vereinprofil_tooltip" id="33" href="/fc-schalke-04/transfers/verein/33/saison_id/2019">FC Schalke 04</a></td>
									<td class="rechts "><a href="/jumplist/transfers/spieler/388058/transfer_id/2463364">ablösefrei</a></td>
									<td class="rechts "><b>No prediction</b></td>
								</tr>
							</tbody>
				</table>
			</div>
										<div class="transfer-zusatzinfo-box">
					<span class="transfer-zusatzinfo-alter">
						Durchschnittsalter der Zugänge: 22,3						</span>
					<span class="transfer-zusatzinfo-wert">
				Gesamtmarktwert der Zugänge: 10,90 Mio. €						</span>
					<span class="transfer-einnahmen-ausgaben redtext">
	Ausgaben: 10,00 Mio. €						</span>
					<br class="clearer" />
				</div>
		</div>
				
				
				<div class="box">
				<div class="table-header" id="to-39"><a class="vereinprofil_tooltip" id="39" href="/1-fsv-mainz-05/transfers/verein/39/saison_id/2019"><img src="https://tmssl.akamaized.net/images/wappen/small/39.png?lm=1564748880" title="&nbsp;" alt="1.FSV Mainz 05" class="" /></a><h2><a class="vereinprofil_tooltip" id="39" href="/1-fsv-mainz-05/transfers/verein/39/saison_id/2019">1.FSV Mainz 05</a></h2></div>
				<div class="responsive-table">
					<table>
						<thead>
							<tr>
								<th class="spieler-transfer-cell">Zugang</th>
								<th class="zentriert alter-transfer-cell">Alter</th>
								<th class="zentriert nat-transfer-cell">Nat.</th>
								<th class="pos-transfer-cell">Position</th>
								<th class="kurzpos-transfer-cell zentriert">Pos</th>
								<th class="rechts mw-transfer-cell">Marktwert</th>
								<th colspan="2" class="verein-transfer-cell">Abgebender Verein</th>
								<th class="rechts abloese-transfer-cell">Ablöse</th>
								<th class="rechts abloese-transfer-cell">Prediction</th>
							</tr>
						</thead>
						<tbody>
																<tr>
										<td><div class="di nowrap"><span class="hide-for-small"><a title="Jeremiah St. Juste" class="spielprofil_tooltip" id="288253" href="/jeremiah-st-juste/profil/spieler/288253">Jeremiah St. Juste</a></span></div><div class="di nowrap"><span class="show-for-small"><a title="Jeremiah St. Juste" class="spielprofil_tooltip" id="288253" href="/jeremiah-st-juste/profil/spieler/288253">J. St. Juste</a></span></div></td>
										<td class="zentriert alter-transfer-cell">22</td>
										<td class="zentriert nat-transfer-cell"><img src="https://tmssl.akamaized.net/images/flagge/tiny/122.png?lm=1520611569" title="Niederlande" alt="Niederlande" class="flaggenrahmen" /><br /><img src="https://tmssl.akamaized.net/images/flagge/tiny/225.png?lm=1520611569" title="St. Kitts und Nevis" alt="St. Kitts und Nevis" class="flaggenrahmen" /></td>
										<td class="pos-transfer-cell">Innenverteidiger</td>
										<td class="kurzpos-transfer-cell zentriert">IV</td>
										<td class="rechts mw-transfer-cell">7,50 Mio. €</td>
										<td class="no-border-rechts zentriert"><a class="vereinprofil_tooltip" id="234" href="/feyenoord-rotterdam/transfers/verein/234/saison_id/2019"><img src="https://tmssl.akamaized.net/images/wappen/tiny/234.png?lm=1457643518" title="&nbsp;" alt="Feyenoord Rotterdam" class="tiny_wappen" /></a></td>
										<td class="no-border-links verein-flagge-transfer-cell"> <img src="https://tmssl.akamaized.net/images/flagge/tiny/122.png?lm=1520611569" title="Niederlande" alt="Niederlande" class="flaggenrahmen" />&nbsp;&nbsp;<a class="vereinprofil_tooltip" id="234" href="/feyenoord-rotterdam/transfers/verein/234/saison_id/2019">Feyenoord</a></td>
										<td class="rechts "><a href="/jumplist/transfers/spieler/288253/transfer_id/2595156">8,00 Mio. €</a></td>
										<td class="rechts "><b>4,00 Mio. €</b></td>
										
									</tr>
											<tr>
										<td><div class="di nowrap"><span class="hide-for-small"><a title="Edimilson Fernandes" class="spielprofil_tooltip" id="247555" href="/edimilson-fernandes/profil/spieler/247555">Edimilson Fernandes</a></span></div><div class="di nowrap"><span class="show-for-small"><a title="Edimilson Fernandes" class="spielprofil_tooltip" id="247555" href="/edimilson-fernandes/profil/spieler/247555">E. Fernandes</a></span></div></td>
										<td class="zentriert alter-transfer-cell">23</td>
										<td class="zentriert nat-transfer-cell"><img src="https://tmssl.akamaized.net/images/flagge/tiny/148.png?lm=1520611569" title="Schweiz" alt="Schweiz" class="flaggenrahmen" /><br /><img src="https://tmssl.akamaized.net/images/flagge/tiny/136.png?lm=1520611569" title="Portugal" alt="Portugal" class="flaggenrahmen" /></td>
										<td class="pos-transfer-cell">Zentrales Mittelfeld</td>
										<td class="kurzpos-transfer-cell zentriert">ZM</td>
										<td class="rechts mw-transfer-cell">8,00 Mio. €</td>
										<td class="no-border-rechts zentriert"><a class="vereinprofil_tooltip" id="379" href="/west-ham-united/transfers/verein/379/saison_id/2019"><img src="https://tmssl.akamaized.net/images/wappen/tiny/379.png?lm=1464675260" title="&nbsp;" alt="West Ham United" class="tiny_wappen" /></a></td>
										<td class="no-border-links verein-flagge-transfer-cell"> <img src="https://tmssl.akamaized.net/images/flagge/tiny/189.png?lm=1520611569" title="England" alt="England" class="flaggenrahmen" />&nbsp;&nbsp;<a class="vereinprofil_tooltip" id="379" href="/west-ham-united/transfers/verein/379/saison_id/2019">West Ham Utd.</a></td>
										<td class="rechts "><a href="/jumplist/transfers/spieler/247555/transfer_id/2493809">7,50 Mio. €</a></td>
										<td class="rechts "><b>5,11 Mio. €</b></td>
									</tr>
											<tr>
										<td><div class="di nowrap"><span class="hide-for-small"><a title="Aarón Martín" class="spielprofil_tooltip" id="251878" href="/aaron-martin/profil/spieler/251878">Aarón Martín</a></span></div><div class="di nowrap"><span class="show-for-small"><a title="Aarón Martín" class="spielprofil_tooltip" id="251878" href="/aaron-martin/profil/spieler/251878">A. Martín</a></span></div></td>
										<td class="zentriert alter-transfer-cell">22</td>
										<td class="zentriert nat-transfer-cell"><img src="https://tmssl.akamaized.net/images/flagge/tiny/157.png?lm=1520611569" title="Spanien" alt="Spanien" class="flaggenrahmen" /></td>
										<td class="pos-transfer-cell">Linker Verteidiger</td>
										<td class="kurzpos-transfer-cell zentriert">LV</td>
										<td class="rechts mw-transfer-cell">20,00 Mio. €</td>
										<td class="no-border-rechts zentriert"><a class="vereinprofil_tooltip" id="714" href="/espanyol-barcelona/transfers/verein/714/saison_id/2019"><img src="https://tmssl.akamaized.net/images/wappen/tiny/714.png?lm=1406966369" title="&nbsp;" alt="Espanyol Barcelona" class="tiny_wappen" /></a></td>
										<td class="no-border-links verein-flagge-transfer-cell"> <img src="https://tmssl.akamaized.net/images/flagge/tiny/157.png?lm=1520611569" title="Spanien" alt="Spanien" class="flaggenrahmen" />&nbsp;&nbsp;<a class="vereinprofil_tooltip" id="714" href="/espanyol-barcelona/transfers/verein/714/saison_id/2019">Esp. Barcelona</a></td>
										<td class="rechts "><a href="/jumplist/transfers/spieler/251878/transfer_id/2305127">6,00 Mio. €</a></td>
										<td class="rechts "><b>3,41 Mio. €</b></td>
									</tr>
											<tr>
										<td><div class="di nowrap"><span class="hide-for-small"><a title="Ronaël Pierre-Gabriel" class="spielprofil_tooltip" id="410185" href="/ronael-pierre-gabriel/profil/spieler/410185">Ronaël Pierre-Gabriel</a></span></div><div class="di nowrap"><span class="show-for-small"><a title="Ronaël Pierre-Gabriel" class="spielprofil_tooltip" id="410185" href="/ronael-pierre-gabriel/profil/spieler/410185">R. Pierre-Gabriel</a></span></div></td>
										<td class="zentriert alter-transfer-cell">21</td>
										<td class="zentriert nat-transfer-cell"><img src="https://tmssl.akamaized.net/images/flagge/tiny/50.png?lm=1520611569" title="Frankreich" alt="Frankreich" class="flaggenrahmen" /></td>
										<td class="pos-transfer-cell">Rechter Verteidiger</td>
										<td class="kurzpos-transfer-cell zentriert">RV</td>
										<td class="rechts mw-transfer-cell">4,00 Mio. €</td>
										<td class="no-border-rechts zentriert"><a class="vereinprofil_tooltip" id="162" href="/as-monaco/transfers/verein/162/saison_id/2019"><img src="https://tmssl.akamaized.net/images/wappen/tiny/162.png?lm=1463176069" title="&nbsp;" alt="AS Monaco" class="tiny_wappen" /></a></td>
										<td class="no-border-links verein-flagge-transfer-cell"> <img src="https://tmssl.akamaized.net/images/flagge/tiny/50.png?lm=1520611569" title="Frankreich" alt="Frankreich" class="flaggenrahmen" />&nbsp;&nbsp;<a class="vereinprofil_tooltip" id="162" href="/as-monaco/transfers/verein/162/saison_id/2019">AS Monaco</a></td>
										<td class="rechts "><a href="/jumplist/transfers/spieler/410185/transfer_id/2507016">5,50 Mio. €</a></td>
										<td class="rechts "><b>4,65 Mio. €</b></td>
									</tr>
											<tr>
										<td><div class="di nowrap"><span class="hide-for-small"><a title="Jonathan Meier" class="spielprofil_tooltip" id="379989" href="/jonathan-meier/profil/spieler/379989">Jonathan Meier</a></span></div><div class="di nowrap"><span class="show-for-small"><a title="Jonathan Meier" class="spielprofil_tooltip" id="379989" href="/jonathan-meier/profil/spieler/379989">J. Meier</a></span></div></td>
										<td class="zentriert alter-transfer-cell">19</td>
										<td class="zentriert nat-transfer-cell"><img src="https://tmssl.akamaized.net/images/flagge/tiny/40.png?lm=1520612525" title="Deutschland" alt="Deutschland" class="flaggenrahmen" /></td>
										<td class="pos-transfer-cell">Linker Verteidiger</td>
										<td class="kurzpos-transfer-cell zentriert">LV</td>
										<td class="rechts mw-transfer-cell">100 Tsd. €</td>
										<td class="no-border-rechts zentriert"><a class="vereinprofil_tooltip" id="28" href="/fc-bayern-munchen-ii/transfers/verein/28/saison_id/2019"><img src="https://tmssl.akamaized.net/images/wappen/tiny/28.png?lm=1498251238" title="&nbsp;" alt="FC Bayern München II" class="tiny_wappen" /></a></td>
										<td class="no-border-links verein-flagge-transfer-cell"> <img src="https://tmssl.akamaized.net/images/flagge/tiny/40.png?lm=1520612525" title="Deutschland" alt="Deutschland" class="flaggenrahmen" />&nbsp;&nbsp;<a class="vereinprofil_tooltip" id="28" href="/fc-bayern-munchen-ii/transfers/verein/28/saison_id/2019">B. München II</a></td>
										<td class="rechts "><a href="/jumplist/transfers/spieler/379989/transfer_id/2486765">1,20 Mio. €</a></td>
										<td class="rechts "><b>1,90 Mio. €</b></td>
									</tr>
											<tr>
										<td><div class="di nowrap"><span class="hide-for-small"><a title="Dong-won Ji" class="spielprofil_tooltip" id="164265" href="/dong-won-ji/profil/spieler/164265">Dong-won Ji</a></span></div><div class="di nowrap"><span class="show-for-small"><a title="Dong-won Ji" class="spielprofil_tooltip" id="164265" href="/dong-won-ji/profil/spieler/164265">D. Ji</a></span></div></td>
										<td class="zentriert alter-transfer-cell">28</td>
										<td class="zentriert nat-transfer-cell"><img src="https://tmssl.akamaized.net/images/flagge/tiny/87.png?lm=1520611569" title="Südkorea" alt="Südkorea" class="flaggenrahmen" /></td>
										<td class="pos-transfer-cell">Mittelstürmer</td>
										<td class="kurzpos-transfer-cell zentriert">MS</td>
										<td class="rechts mw-transfer-cell">1,75 Mio. €</td>
										<td class="no-border-rechts zentriert"><a class="vereinprofil_tooltip" id="167" href="/fc-augsburg/transfers/verein/167/saison_id/2019"><img src="https://tmssl.akamaized.net/images/wappen/tiny/167.png?lm=1403085893" title="&nbsp;" alt="FC Augsburg" class="tiny_wappen" /></a></td>
										<td class="no-border-links verein-flagge-transfer-cell"> <img src="https://tmssl.akamaized.net/images/flagge/tiny/40.png?lm=1520612525" title="Deutschland" alt="Deutschland" class="flaggenrahmen" />&nbsp;&nbsp;<a class="vereinprofil_tooltip" id="167" href="/fc-augsburg/transfers/verein/167/saison_id/2019">FC Augsburg</a></td>
										<td class="rechts "><a href="/jumplist/transfers/spieler/164265/transfer_id/2467550">ablösefrei</a></td>
										<td class="rechts "><b>No prediction</b></td>
									</tr>
											<tr>
										<td><div class="di nowrap"><span class="hide-for-small"><a title="Omer Hanin" class="spielprofil_tooltip" id="211530" href="/omer-hanin/profil/spieler/211530">Omer Hanin</a></span></div><div class="di nowrap"><span class="show-for-small"><a title="Omer Hanin" class="spielprofil_tooltip" id="211530" href="/omer-hanin/profil/spieler/211530">O. Hanin</a></span></div></td>
										<td class="zentriert alter-transfer-cell">21</td>
										<td class="zentriert nat-transfer-cell"><img src="https://tmssl.akamaized.net/images/flagge/tiny/74.png?lm=1520611569" title="Israel" alt="Israel" class="flaggenrahmen" /><br /><img src="https://tmssl.akamaized.net/images/flagge/tiny/136.png?lm=1520611569" title="Portugal" alt="Portugal" class="flaggenrahmen" /></td>
										<td class="pos-transfer-cell">Torwart</td>
										<td class="kurzpos-transfer-cell zentriert">TW</td>
										<td class="rechts mw-transfer-cell">300 Tsd. €</td>
										<td class="no-border-rechts zentriert"><a class="vereinprofil_tooltip" id="51931" href="/hapoel-hadera-givat-olga/transfers/verein/51931/saison_id/2019"><img src="https://tmssl.akamaized.net/images/wappen/tiny/51931.png?lm=1455345876" title="&nbsp;" alt="Hapoel Hadera" class="tiny_wappen" /></a></td>
										<td class="no-border-links verein-flagge-transfer-cell"> <img src="https://tmssl.akamaized.net/images/flagge/tiny/74.png?lm=1520611569" title="Israel" alt="Israel" class="flaggenrahmen" />&nbsp;&nbsp;<a class="vereinprofil_tooltip" id="51931" href="/hapoel-hadera-givat-olga/transfers/verein/51931/saison_id/2019">Hapoel Hadera</a></td>
										<td class="rechts "><a href="/jumplist/transfers/spieler/211530/transfer_id/2478541">ablösefrei</a></td>
										<td class="rechts "><b>No prediction</b></td>
									</tr>
											<tr>
										<td><div class="di nowrap"><span class="hide-for-small"><a title="Ádám Szalai" class="spielprofil_tooltip" id="39106" href="/adam-szalai/profil/spieler/39106">Ádám Szalai</a></span></div><div class="di nowrap"><span class="show-for-small"><a title="Ádám Szalai" class="spielprofil_tooltip" id="39106" href="/adam-szalai/profil/spieler/39106">Á. Szalai</a></span></div></td>
										<td class="zentriert alter-transfer-cell">31</td>
										<td class="zentriert nat-transfer-cell"><img src="https://tmssl.akamaized.net/images/flagge/tiny/178.png?lm=1521635893" title="Ungarn" alt="Ungarn" class="flaggenrahmen" /></td>
										<td class="pos-transfer-cell">Mittelstürmer</td>
										<td class="kurzpos-transfer-cell zentriert">MS</td>
										<td class="rechts mw-transfer-cell">3,00 Mio. €</td>
										<td class="no-border-rechts zentriert"><a class="vereinprofil_tooltip" id="533" href="/tsg-1899-hoffenheim/transfers/verein/533/saison_id/2019"><img src="https://tmssl.akamaized.net/images/wappen/tiny/533.png?lm=1458907862" title="&nbsp;" alt="TSG 1899 Hoffenheim" class="tiny_wappen" /></a></td>
										<td class="no-border-links verein-flagge-transfer-cell"> <img src="https://tmssl.akamaized.net/images/flagge/tiny/40.png?lm=1520612525" title="Deutschland" alt="Deutschland" class="flaggenrahmen" />&nbsp;&nbsp;<a class="vereinprofil_tooltip" id="533" href="/tsg-1899-hoffenheim/transfers/verein/533/saison_id/2019">TSG Hoffenheim</a></td>
										<td class="rechts "><a href="/jumplist/transfers/spieler/39106/transfer_id/2624065">ablösefrei</a></td>
										<td class="rechts "><b>No prediction</b></td>
									</tr>
								</tbody>
					</table>
				</div>
											<div class="transfer-zusatzinfo-box">
						<span class="transfer-zusatzinfo-alter">
							Durchschnittsalter der Zugänge: 23,4						</span>
						<span class="transfer-zusatzinfo-wert">
					Gesamtmarktwert der Zugänge: 44,65 Mio. €						</span>
						<span class="transfer-einnahmen-ausgaben redtext">
		Ausgaben: 28,20 Mio. €						</span>
						<br class="clearer" />
			</div>

				<div class="box">
				<div class="table-header" id="to-3"><a class="vereinprofil_tooltip" id="3" href="/1-fc-koln/transfers/verein/3/saison_id/2019"><img src="https://tmssl.akamaized.net/images/wappen/small/3.png?lm=1396275280" title="&nbsp;" alt="1.FC Köln" class="" /></a><h2><a class="vereinprofil_tooltip" id="3" href="/1-fc-koln/transfers/verein/3/saison_id/2019">1.FC Köln</a></h2></div>
				<div class="responsive-table">
					<table>
						<thead>
							<tr>
								<th class="spieler-transfer-cell">Zugang</th>
								<th class="zentriert alter-transfer-cell">Alter</th>
								<th class="zentriert nat-transfer-cell">Nat.</th>
								<th class="pos-transfer-cell">Position</th>
								<th class="kurzpos-transfer-cell zentriert">Pos</th>
								<th class="rechts mw-transfer-cell">Marktwert</th>
								<th colspan="2" class="verein-transfer-cell">Abgebender Verein</th>
								<th class="rechts abloese-transfer-cell">Ablöse</th>
								<th class="rechts abloese-transfer-cell">Prediction</th>
							</tr>
						</thead>
						<tbody>
																<tr>
										<td><div class="di nowrap"><span class="hide-for-small"><a title="Ellyes Skhiri" class="spielprofil_tooltip" id="290587" href="/ellyes-skhiri/profil/spieler/290587">Ellyes Skhiri</a></span></div><div class="di nowrap"><span class="show-for-small"><a title="Ellyes Skhiri" class="spielprofil_tooltip" id="290587" href="/ellyes-skhiri/profil/spieler/290587">E. Skhiri</a></span></div></td>
										<td class="zentriert alter-transfer-cell">24</td>
										<td class="zentriert nat-transfer-cell"><img src="https://tmssl.akamaized.net/images/flagge/tiny/173.png?lm=1520611569" title="Tunesien" alt="Tunesien" class="flaggenrahmen" /><br /><img src="https://tmssl.akamaized.net/images/flagge/tiny/50.png?lm=1520611569" title="Frankreich" alt="Frankreich" class="flaggenrahmen" /></td>
										<td class="pos-transfer-cell">Defensives Mittelfeld</td>
										<td class="kurzpos-transfer-cell zentriert">DM</td>
										<td class="rechts mw-transfer-cell">12,00 Mio. €</td>
										<td class="no-border-rechts zentriert"><a class="vereinprofil_tooltip" id="969" href="/hsc-montpellier/transfers/verein/969/saison_id/2019"><img src="https://tmssl.akamaized.net/images/wappen/tiny/969.png?lm=1459072367" title="&nbsp;" alt="Montpellier HSC" class="tiny_wappen" /></a></td>
										<td class="no-border-links verein-flagge-transfer-cell"> <img src="https://tmssl.akamaized.net/images/flagge/tiny/50.png?lm=1520611569" title="Frankreich" alt="Frankreich" class="flaggenrahmen" />&nbsp;&nbsp;<a class="vereinprofil_tooltip" id="969" href="/hsc-montpellier/transfers/verein/969/saison_id/2019">Montpellier</a></td>
										<td class="rechts "><a href="/jumplist/transfers/spieler/290587/transfer_id/2580110">6,00 Mio. €</a></td>
										<td class="rechts "><b>4,73 Mio. €</b></td>
									</tr>
											<tr>
										<td><div class="di nowrap"><span class="hide-for-small"><a title="Sebastiaan Bornauw" class="spielprofil_tooltip" id="338629" href="/sebastiaan-bornauw/profil/spieler/338629">Sebastiaan Bornauw</a></span></div><div class="di nowrap"><span class="show-for-small"><a title="Sebastiaan Bornauw" class="spielprofil_tooltip" id="338629" href="/sebastiaan-bornauw/profil/spieler/338629">S. Bornauw</a></span></div></td>
										<td class="zentriert alter-transfer-cell">20</td>
										<td class="zentriert nat-transfer-cell"><img src="https://tmssl.akamaized.net/images/flagge/tiny/19.png?lm=1520611569" title="Belgien" alt="Belgien" class="flaggenrahmen" /></td>
										<td class="pos-transfer-cell">Innenverteidiger</td>
										<td class="kurzpos-transfer-cell zentriert">IV</td>
										<td class="rechts mw-transfer-cell">4,00 Mio. €</td>
										<td class="no-border-rechts zentriert"><a class="vereinprofil_tooltip" id="58" href="/rsc-anderlecht/transfers/verein/58/saison_id/2019"><img src="https://tmssl.akamaized.net/images/wappen/tiny/58.png?lm=1443857722" title="&nbsp;" alt="RSC Anderlecht" class="tiny_wappen" /></a></td>
										<td class="no-border-links verein-flagge-transfer-cell"> <img src="https://tmssl.akamaized.net/images/flagge/tiny/19.png?lm=1520611569" title="Belgien" alt="Belgien" class="flaggenrahmen" />&nbsp;&nbsp;<a class="vereinprofil_tooltip" id="58" href="/rsc-anderlecht/transfers/verein/58/saison_id/2019">RSC Anderlecht</a></td>
										<td class="rechts "><a href="/jumplist/transfers/spieler/338629/transfer_id/2592752">6,00 Mio. €</a></td>
										<td class="rechts "><b>6,72 Mio. €</b></td>
									</tr>
											<tr>
										<td><div class="di nowrap"><span class="hide-for-small"><a title="Birger Verstraete" class="spielprofil_tooltip" id="234193" href="/birger-verstraete/profil/spieler/234193">Birger Verstraete</a></span></div><div class="di nowrap"><span class="show-for-small"><a title="Birger Verstraete" class="spielprofil_tooltip" id="234193" href="/birger-verstraete/profil/spieler/234193">B. Verstraete</a></span></div></td>
										<td class="zentriert alter-transfer-cell">25</td>
										<td class="zentriert nat-transfer-cell"><img src="https://tmssl.akamaized.net/images/flagge/tiny/19.png?lm=1520611569" title="Belgien" alt="Belgien" class="flaggenrahmen" /></td>
										<td class="pos-transfer-cell">Defensives Mittelfeld</td>
										<td class="kurzpos-transfer-cell zentriert">DM</td>
										<td class="rechts mw-transfer-cell">4,00 Mio. €</td>
										<td class="no-border-rechts zentriert"><a class="vereinprofil_tooltip" id="157" href="/kaa-gent/transfers/verein/157/saison_id/2019"><img src="https://tmssl.akamaized.net/images/wappen/tiny/157.png?lm=1442954733" title="&nbsp;" alt="KAA Gent" class="tiny_wappen" /></a></td>
										<td class="no-border-links verein-flagge-transfer-cell"> <img src="https://tmssl.akamaized.net/images/flagge/tiny/19.png?lm=1520611569" title="Belgien" alt="Belgien" class="flaggenrahmen" />&nbsp;&nbsp;<a class="vereinprofil_tooltip" id="157" href="/kaa-gent/transfers/verein/157/saison_id/2019">KAA Gent</a></td>
										<td class="rechts "><a href="/jumplist/transfers/spieler/234193/transfer_id/2511346">4,00 Mio. €</a></td>
										<td class="rechts "><b>3,11 Mio. €</b></td>
									</tr>
											<tr>
										<td><div class="di nowrap"><span class="hide-for-small"><a title="Kingsley Ehizibue" class="spielprofil_tooltip" id="272812" href="/kingsley-ehizibue/profil/spieler/272812">Kingsley Ehizibue</a></span></div><div class="di nowrap"><span class="show-for-small"><a title="Kingsley Ehizibue" class="spielprofil_tooltip" id="272812" href="/kingsley-ehizibue/profil/spieler/272812">K. Ehizibue</a></span></div></td>
										<td class="zentriert alter-transfer-cell">24</td>
										<td class="zentriert nat-transfer-cell"><img src="https://tmssl.akamaized.net/images/flagge/tiny/124.png?lm=1520611569" title="Nigeria" alt="Nigeria" class="flaggenrahmen" /><br /><img src="https://tmssl.akamaized.net/images/flagge/tiny/122.png?lm=1520611569" title="Niederlande" alt="Niederlande" class="flaggenrahmen" /></td>
										<td class="pos-transfer-cell">Rechter Verteidiger</td>
										<td class="kurzpos-transfer-cell zentriert">RV</td>
										<td class="rechts mw-transfer-cell">2,00 Mio. €</td>
										<td class="no-border-rechts zentriert"><a class="vereinprofil_tooltip" id="1269" href="/pec-zwolle/transfers/verein/1269/saison_id/2019"><img src="https://tmssl.akamaized.net/images/wappen/tiny/1269.png?lm=1586974571" title="&nbsp;" alt="PEC Zwolle" class="tiny_wappen" /></a></td>
										<td class="no-border-links verein-flagge-transfer-cell"> <img src="https://tmssl.akamaized.net/images/flagge/tiny/122.png?lm=1520611569" title="Niederlande" alt="Niederlande" class="flaggenrahmen" />&nbsp;&nbsp;<a class="vereinprofil_tooltip" id="1269" href="/pec-zwolle/transfers/verein/1269/saison_id/2019">PEC Zwolle</a></td>
										<td class="rechts "><a href="/jumplist/transfers/spieler/272812/transfer_id/2491564">2,00 Mio. €</a></td>
										<td class="rechts "><b>2,73 Mio. €</b></td>
									</tr>
											<tr>
										<td><div class="di nowrap"><span class="hide-for-small"><a title="Kingsley Schindler" class="spielprofil_tooltip" id="153678" href="/kingsley-schindler/profil/spieler/153678">Kingsley Schindler</a></span></div><div class="di nowrap"><span class="show-for-small"><a title="Kingsley Schindler" class="spielprofil_tooltip" id="153678" href="/kingsley-schindler/profil/spieler/153678">K. Schindler</a></span></div></td>
										<td class="zentriert alter-transfer-cell">25</td>
										<td class="zentriert nat-transfer-cell"><img src="https://tmssl.akamaized.net/images/flagge/tiny/40.png?lm=1520612525" title="Deutschland" alt="Deutschland" class="flaggenrahmen" /><br /><img src="https://tmssl.akamaized.net/images/flagge/tiny/54.png?lm=1520611569" title="Ghana" alt="Ghana" class="flaggenrahmen" /></td>
										<td class="pos-transfer-cell">Rechtsaußen</td>
										<td class="kurzpos-transfer-cell zentriert">RA</td>
										<td class="rechts mw-transfer-cell">3,00 Mio. €</td>
										<td class="no-border-rechts zentriert"><a class="vereinprofil_tooltip" id="269" href="/holstein-kiel/transfers/verein/269/saison_id/2019"><img src="https://tmssl.akamaized.net/images/wappen/tiny/269.png?lm=1544480289" title="&nbsp;" alt="Holstein Kiel" class="tiny_wappen" /></a></td>
										<td class="no-border-links verein-flagge-transfer-cell"> <img src="https://tmssl.akamaized.net/images/flagge/tiny/40.png?lm=1520612525" title="Deutschland" alt="Deutschland" class="flaggenrahmen" />&nbsp;&nbsp;<a class="vereinprofil_tooltip" id="269" href="/holstein-kiel/transfers/verein/269/saison_id/2019">Holstein Kiel</a></td>
										<td class="rechts "><a href="/jumplist/transfers/spieler/153678/transfer_id/2370603">ablösefrei</a></td>
										<td class="rechts "><b>No prediction</b></td>
									</tr>
											<tr>
										<td><div class="di nowrap"><span class="hide-for-small"><a title="Julian Krahl" class="spielprofil_tooltip" id="337082" href="/julian-krahl/profil/spieler/337082">Julian Krahl</a></span></div><div class="di nowrap"><span class="show-for-small"><a title="Julian Krahl" class="spielprofil_tooltip" id="337082" href="/julian-krahl/profil/spieler/337082">J. Krahl</a></span></div></td>
										<td class="zentriert alter-transfer-cell">19</td>
										<td class="zentriert nat-transfer-cell"><img src="https://tmssl.akamaized.net/images/flagge/tiny/40.png?lm=1520612525" title="Deutschland" alt="Deutschland" class="flaggenrahmen" /></td>
										<td class="pos-transfer-cell">Torwart</td>
										<td class="kurzpos-transfer-cell zentriert">TW</td>
										<td class="rechts mw-transfer-cell">200 Tsd. €</td>
										<td class="no-border-rechts zentriert"><a class="vereinprofil_tooltip" id="23826" href="/rasenballsport-leipzig/transfers/verein/23826/saison_id/2019"><img src="https://tmssl.akamaized.net/images/wappen/tiny/23826_1594040076.png?lm=1594040033" title="&nbsp;" alt="RasenBallsport Leipzig" class="" /></a></td>
										<td class="no-border-links verein-flagge-transfer-cell"> <img src="https://tmssl.akamaized.net/images/flagge/tiny/40.png?lm=1520612525" title="Deutschland" alt="Deutschland" class="flaggenrahmen" />&nbsp;&nbsp;<a class="vereinprofil_tooltip" id="23826" href="/rasenballsport-leipzig/transfers/verein/23826/saison_id/2019">RB Leipzig</a></td>
										<td class="rechts "><a href="/jumplist/transfers/spieler/337082/transfer_id/2476421">ablösefrei</a></td>
										<td class="rechts "><b>No prediction</b></td>
									</tr>
								</tbody>
					</table>
				</div>
											<div class="transfer-zusatzinfo-box">
						<span class="transfer-zusatzinfo-alter">
							Durchschnittsalter der Zugänge: 22,8						</span>
						<span class="transfer-zusatzinfo-wert">
					Gesamtmarktwert der Zugänge: 25,20 Mio. €						</span>
						<span class="transfer-einnahmen-ausgaben redtext">
		Ausgaben: 18,00 Mio. €						</span>
						<br class="clearer" />
					
			</div>

							</div>
			</div>

		</div>
		
</div>
				</div>
	</div>

</body>
</html>


'''