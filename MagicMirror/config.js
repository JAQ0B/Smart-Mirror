let config = {
	address: "0.0.0.0",	
	port: 8080,
	basePath: "/",	
	ipWhitelist: [],	

	useHttps: false,			
	httpsPrivateKey: "",	
	httpsCertificate: "",	

	language: "en",
	locale: "en-US",
	logLevel: ["INFO", "LOG", "WARN", "ERROR"], 
	timeFormat: 24,
	units: "metric",

	modules: [
		{
			module: 'MMM-Remote-Control',
			position: 'bottom_left',
			config: {
				apiKey: 'XXXX',
				customCommand: {},  
				showModuleApiMenu: true, 
				secureEndpoints: true, 
			}
		},
		{
			module: 'MMM-pages',
			config: {
					modules:
						[[ "MMM-Remote-Control", "calendar", "weather" ],
						 [ "MMM-OnSpotify", "MMM-LiveLyrics" ],
						 [ "MMM-ImagesPhotos", "weather", "MMM-WeatherDependentClothes", "MMM-SimpleLogo" ],
						 [ "MMM-YrThen", "weather", "mmm-weatherchart", "MMM-WeatherBackground" ],
						],
					fixed: [ "clock", "MMM-page-indicator" ],
					hiddenPages: {
						"screenSaver": [ "clock", "MMM-SomeBackgroundImageModule" ],
						"admin": [ "MMM-ShowMeSystemStatsModule", "MMM-AnOnScreenMenuModule" ],
					},
			}
		},
				{
			module: 'MMM-page-indicator',
			position: 'bottom_bar',
			config: {
				pages: 4,	
			}
		},
		{
			module: "clock",
			position: "top_left",
			    config: {
					displaySeconds: false,
					showDate: true,
					
				},	
		},
		{
			module: "weather",
			position: "top_right",
			config: {
				weatherProvider: "openweathermap",
				type: "current",
				location: "Vejle",
				locationID: "2610601", 
				apiKey: "XXXX",
				decimalSymbol: "",
				roundTemp: true,
				showFeelsLike: false
			}
		},
		{
		module: 'mmm-weatherchart',
		position: 'top_left', // this can be any of the regions
		config: {
			locationPath: "https://www.yr.no/en/content/2-2610613/meteogram.svg",
			updateInterval: 60 * 60 * 1000, // update every hour
			hideBorder: true, 
			negativeImage: true, 
			hoursToShow: 24, 
			mmDirectory: "/home/SmartMirror/MagicMirror/"
			}
		},
		{
			module: 'MMM-YrThen',
			position: 'top_left',
				config: {
					location: '2-2610613',
					windUnit: "m/s",
					maxMinSeparator: "/",
					numDays: 5,
										
				}
		},
		{
			module: "calendar",
			header: "Kalender",
			position: "top_right",
			config: {
				calendars: [
					{
						fetchInterval: 1 * 200 * 1 * 1 * 1000,
						symbol: "Kalender",
						url: "XXXX"
					}
				],
				maximumEntries: 20,
				showLocation: true,
				customEvents: [{keyword: 'Fødselsdag', symbol: 'birthday-cake', color: '#d3ad04de'},
								{keyword: 'Eksamen', symbol: 'graduation-cap', color: '#b31b01'}
								] //  https://fontawesome.com/v6/search?o=r&m=free&c=education for symbols
				
			}
		},
		{
        module: "MMM-SimpleLogo",
        position: 'middle_center',    // This can be any of the regions.
			config: {
				refreshInterval: 1000,
				width: '620px',
				text: "",
			}
		},
		{
			module: "MMM-ImagesPhotos",
			position: "middle_center",
			config: {
			 opacity: 0.9,
			 animationSpeed: 0,
			 updateInterval: 1000,
			 getInterval: 1000,
			 maxHeight: "700px",
			 maxWidth:"700px",
			 sequential: false  // process the image list randomly
			}
		},
		{
		module: "MMM-WeatherDependentClothes",
		position: "top_right", // This can be any of the regions.
			config: {
			// See 'Configuration options' for more information.
			location: "Vejle",
			locationID: "2610601", 
			appid: "XXX", 
			preferences: [
				{
				    name: "Winter jacket",
				    icon: "jacket-cold",
				    conditions: {
					temp_max: 2.0,
				    }
				},
				// more items here. See .js for default list
			]
			}
		},
		{
			module: "MMM-OnSpotify",
			position: "top_left",
			config: {
				// Spotify authentication (Authentication Service)
				clientID: "XXXX",
				clientSecret: "XXXX",
				accessToken: "XXXX",
				refreshToken: "XXXX",
				// General module options [SEE BELOW]
				displayWhenEmpty: "both",
				userAffinityUseTracks: false,
				prefersLargeImageSize: false,
				hideTrackLenghtAndAnimateProgress: false,
				showDebugPalette: false,
				userDataMaxAge: 14400,
				userAffinityMaxAge: 36000,
				deviceFilter: [],
				deviceFilterExclude: false,
				filterNoticeSubtitle: true,
				// Update intervals [SEE BELOW]
				isPlaying: 1,
				isEmpty: 2,
				isPlayingHidden: 2,
				isEmptyHidden: 4,
				onReconnecting: 4,
				onError: 8,
				// Animations [SEE BELOW]
				mediaAnimations: false,
				fadeAnimations: false,
				textAnimations: false,
				transitionAnimations: true,
				// Spotify Code (EXPERMIENTAL)
				spotifyCodeExperimentalShow: true,
				spotifyCodeExperimentalUseColor: true,
				spotifyCodeExperimentalSeparateItem: true,
				// Theming General
				roundMediaCorners: true,
				roundProgressBar: true,
				showVerticalPipe: true, 
				useColorInProgressBar: true,
				useColorInTitle: true,
				useColorInUserData: true,
				showBlurBackground: true,
				blurCorrectionInFrameSide: false,
				blurCorrectionInAllSides: false,
				alwaysUseDefaultDeviceIcon: false,
				experimentalCSSOverridesForMM2: true, 
			}
		},
		{
			// This is the base config. See more config options below
			module: "MMM-LiveLyrics",
			position: "fullscreen_below", // Do not change position
			config: {
				accessToken: "XXXX", 
				useDefaultSearchFormatter: true,
				useMultipleArtistInSearch: true,
				logSuspendResume: false,
				showConnectionQrOnLoad: false,
				connectionQrDuration: 12,
				sideBySideOnLandscape: false,
				startHidden: true,
				hideSpotifyModule: true,
				updateTopModulesCalcOnData: true,

				// Lyrics style [See below]
				lyricsFillType: "containerCalcTopModules",
				lyricsContainerBackdropStyle: "black",
				lyricsStyleTheme: "normal",
				lyricsFontName: null,
				lyricsFontSize: null,
				lyricsTextAlign: null,
				lyricsCustomFixedDimentions: false,

				// Scroll and others [See below]
				scrollStrategy: "bySections",
				scrollUpdateEvery: 3,
				hideStrategy: "flex",
				blurToBlackOnFull: false,
				useAnimations: false,		

 
			  }
			},
			//{ // kan bruges hvis man vil have baggrund der beskriver vejret. Vil åbenbart ikke samarbejde med pages modulet.
			//	module: "MMM-WeatherBackground",
			//
			//	config: {}
			//},
		]
};

/*************** DO NOT EDIT THE LINE BELOW ***************/
if (typeof module !== "undefined") { module.exports = config; }

