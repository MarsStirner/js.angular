from fanstatic import Library, Resource

library = Library('angularjs', 'resources')

angular = Resource(library, 'angular.js', minified='angular.min.js')
angular_animate = Resource(
    library, 'angular-animate.js',
    minified='angular-animate.min.js',
    depends=[angular]
)
angular_aria = Resource(
    library, 'angular-aria.js',
    minified='angular-aria.min.js',
    depends=[angular]
)
angular_cookies = Resource(
    library, 'angular-cookies.js',
    minified='angular-cookies.min.js',
    depends=[angular]
)
angular_csp = Resource(
    library, 'angular-csp.css',
    depends=[angular]
)
angular_loader = Resource(
    library, 'angular-loader.js',
    minified='angular-loader.min.js'
)
angular_message_format = Resource(
    library, 'angular-message-format.js',
    minified='angular-message-format.min.js',
    depends=[angular]
)
angular_messages = Resource(
    library, 'angular-messages.js',
    minified='angular-messages.min.js',
    depends=[angular]
)
angular_mocks = Resource(
    library, 'angular-mocks.js',
    depends=[angular])
angular_resource = Resource(
    library, 'angular-resource.js',
    minified='angular-resource.min.js',
    depends=[angular])
angular_route = Resource(
    library, 'angular-route.js',
    minified='angular-route.min.js',
    depends=[angular])
angular_sanitize = Resource(
    library, 'angular-sanitize.js',
    minified='angular-sanitize.min.js',
    depends=[angular])
angular_scenario = Resource(library, 'angular-scenario.js')
angular_touch = Resource(
    library, 'angular-touch.js',
    minified='angular-touch.min.js',
    depends=[angular])

_langs = [
    'brx', 'ia', 'en-mp', 'de-de', 'az-cyrl-az', 'smn-fi', 'en-dg', 'ps-af', 'or-in', 'ar-so', 'uz', 'saq', 'sw-tz',
    'en-gd', 'mr', 'teo', 'nl', 'lag-tz', 'ar-mr', 'ky-cyrl-kg', 'ksb-tz', 'id-id', 'fr-pm', 'mk', 'es-hn', 'en-ag',
    'gsw-fr', 'en-sd', 'ff', 'ti-er', 'mgo-cm', 'ebu', 'mas-tz', 'es-cr', 'lo', 'ro-md', 'fi', 'eu', 'ckb-arab-ir',
    'fr-sy', 'kn-in', 'vun', 'mk-mk', 'es-sv', 'ru-md', 'zh-hans-hk', 'ja', 'nyn', 'jmc-tz', 'lb-lu', 'fr-gp', 'be',
    'fr-dz', 'byn', 'fr-gf', 'en-vg', 'kea', 'ne-np', 'to-to', 'ia-fr', 'kok-in', 'lv-lv', 'naq-na', 'en-bm', 'ml-in',
    'mfe', 'af-na', 'ln-cg', 'khq-ml', 'ar-ma', 'fr-td', 'en-001', 'nl-be', 'mgh', 'gl-es', 'fr', 'en-vc', 'dyo',
    'ckb-iq', 'ha-latn', 'sw-cd', 'en-zm', 'en-au', 'sr-cyrl-me', 'ne-in', 'ar-ss', 'en-mg', 'nso', 'sbp-tz', 'en-mt',
    'sq-xk', 'si', 'om', 'hu', 'vai-latn', 'en-ki', 'sw-ug', 'en-mo', 'ki-ke', 'en-to', 'pa', 'rn-bi', 'cs-cz',
    'pa-guru-in', 'rm', 'pt-mz', 'as', 'az-cyrl', 'zh-hant-mo', 'th', 'af-za', 'es-419', 'en-sh', 'en-us', 'lv',
    'ee-gh', 'vi', 'fr-cd', 'en-jm', 'ksf', 'de-ch', 'lg-ug', 'xh-za', 'ss-sz', 'en-sb', 'zgh-ma', 'en-na', 'es-ea',
    'sr-cyrl-rs', 'zu', 'ha', 'fr-dj', 'bs-latn-ba', 'ses-ml', 'yo-ng', 'en-gg', 'nb', 'shi-latn-ma', 'so-ke', 'ssy-er',
    'ses', 'om-et', 'nus-sd', 'uz-arab-af', 'es-es', 'en-gm', 'bn-bd', 'mer-ke', 'chr-us', 'en-ie', 'ar-om', 'zh',
    'az-latn', 'fr-mq', 'fr-km', 'ca', 'uz-latn-uz', 'dav-ke', 'ms-latn-bn', 'th-th', 'ckb-ir', 'es-pe', 'sk', 'ms',
    'en-pg', 'ur', 'sr-cyrl-xk', 'os-ru', 'en-tk', 'naq', 'ks', 'so-et', 'it-ch', 'ee-tg', 'vun-tz', 'ewo-cm', 'kw-gb',
    'cgg-ug', 'en-cm', 'bo-cn', 'fil', 'hr', 'en-gu', 'ru-kz', 'bs', 'ar-eg', 'en-pk', 'cs', 'pt', 'en-kn', 'en-bz',
    'bo-in', 'fr-ma', 'shi', 'sq-mk', 'fr-re', 'tzm-latn-ma', 'es-pa', 'yi', 'ar-lb', 'pt-ao', 'mas', 'sl',
    'ha-latn-ng', 'en-tv', 'en-hk', 'fr-mg', 'zh-hans-cn', 'ar-dj', 'is', 'shi-tfng', 'fo', 'fr-nc', 'ta-in', 'ar-iq',
    'mas-ke', 'iw', 'pt-gw', 'ss', 'ln-ao', 'haw', 'en-im', 'saq-ke', 'ff-cm', 'fr-pf', 'rn', 'jgo', 'ug', 'gsw-ch',
    'twq-ne', 'cgg', 'en-ky', 'lt-lt', 'se-fi', 'os-ge', 'en-nr', 'ky-cyrl', 'en-lr', 'kkj', 'fr-lu', 'ky', 'ii-cn',
    'ur-pk', 'vi-vn', 'my', 'ig', 'fo-fo', 'nb-no', 'tg-cyrl', 'ro', 'en-ms', 'zh-hant-tw', 'nb-sj', 'ta-my', 'mgh-mz',
    'rof', 'lu', 'ms-latn-sg', 'tn', 'fy', 'is-is', 'br', 've-za', 'kab', 'en-ca', 'it-sm', 'ff-gn', 'gl', 'id', 'nmg',
    'gsw-li', 'pa-arab', 'en-fj', 'bs-cyrl', 'mt', 'bn-in', 'es-us', 'byn-er', 'yo', 'es-ec', 'en-vi', 'en-nz', 'tig',
    'eo-001', 'twq', 'rof-tz', 'rw', 'cy', 'ne', 'ee', 'kam-ke', 'om-ke', 'fr-tg', 'so-so', 'ha-latn-gh', 'en-gi', 'st',
    'dje', 'en-bb', 'he-il', 'sq-al', 'en-mw', 'fr-ca', 'en-nf', 'tg', 'ru', 'en-rw', 'kde', 'tl', 'ca-it',
    'ckb-latn-iq', 'it', 'mua-cm', 'en-ls', 'mg', 'en-be', 'es-do', 'kln', 'en-ng', 'en-je', 'uz-cyrl-uz', 'bas',
    'en-bs', 'pt-pt', 'fr-ga', 'sg', 'fr-rw', 'se', 'sr-latn', 'ast', 'en-cx', 'seh-mz', 'en-lc', 'bo', 'wal', 'vo',
    'da-gl', 'yav', 'et', 'uk-ua', 'bs-latn', 'es-pr', 'ar-er', 'zh-hk', 'en-fk', 'en-mh', 'en-iso', 'ar-ly', 'dz',
    'lag', 'ug-arab-cn', 'zh-hant-hk', 'gd-gb', 'ko', 'sr-latn-xk', 'ru-ru', 'xog-ug', 'rw-rw', 'ar-il', 'tg-cyrl-tj',
    'am', 'hsb-de', 'sw', 'dz-bt', 'no-no', 'fr-be', 'vo-001', 'pl', 'sah', 'es-ic', 'en-ck', 'ln-cf', 'el-gr', 'nl-sr',
    'luo', 'ko-kr', 'en-um', 'fr-wf', 'fr-ci', 'no', 'gu-in', 'mer', 'chr', 'lt', 'ebu-ke', 'ti', 'en-my', 'mt-mt',
    'gsw', 'so', 'sv-se', 'en-ph', 'pa-guru', 'to', 'zh-hant', 'si-lk', 'dyo-sn', 'zh-cn', 'es-ve', 'es-cu', 'fr-gq',
    'pl-pl', 'ug-arab', 'te', 'el', 'kln-ke', 'ak', 'mua', 'en-io', 'af', 'aa-er', 'es-co', 'tr', 'nr-za', 'fr-bj',
    'cy-gb', 'bm-latn', 'luy-ke', 'hy-am', 'ig-ng', 'bm-ml', 'nd-zw', 'el-cy', 'mfe-mu', 'mn', 'kw', 'lo-la', 'ar-sa',
    'dje-ne', 'hsb', 'az-latn-az', 'be-by', 'ckb-arab-iq', 'lg', 'ti-et', 'ru-by', 'en-tz', 'ar-bh', 'fr-bi', 'ar-td',
    'es-bo', 'or', 'es-ni', 'fa-af', 'eo', 'ksh', 'teo-ke', 'en-za', 'pt-st', 'en-pn', 'tig-er', 'km', 'nso-za',
    'nl-bq', 'pt-tl', 'en-gh', 'uz-latn', 'es-gq', 'kab-dz', 'en-pw', 'bn', 'bem-zm', 'ga', 'ar-ae', 'aa-dj', 'zh-hans',
    'kk', 'fr-cm', 'dav', 'pt-br', 'eu-es', 'mn-cyrl-mn', 'sg-cf', 'my-mm', 'fi-fi', 'rwk-tz', 'fur-it', 'jgo-cm',
    'rm-ch', 'zh-hans-sg', 'os', 'lkt', 'tr-cy', 'pt-mo', 'de', 'ml', 'uk', 'hr-ba', 'pt-cv', 'en-sz', 'guz', 'teo-ug',
    'ar-sd', 'nnh', 'sq', 'nnh-cm', 'ur-in', 'st-ls', 'lkt-us', 'am-et', 'aa', 'wal-et', 'es-uy', 'ms-latn', 'tn-bw',
    'ss-za', 'sr-cyrl', 'he', 'fr-sc', 'te-in', 'bez', 'sv', 'mr-in', 'sr-latn-rs', 'kk-cyrl', 'qu-ec', 'kn', 'fr-mf',
    'shi-tfng-ma', 'en-fm', 'en-ss', 'ssy', 'hi', 'asa-tz', 'ar-jo', 'nl-sx', 'qu-pe', 'se-se', 'en-pr', 'ln-cd', 'gv',
    'en-dm', 'wae', 'sk-sk', 'en-gy', 'ff-sn', 'ca-fr', 'ta-lk', 'ts', 'ckb-arab', 'kde-tz', 'swc', 'gv-im', 'wae-ch',
    'sbp', 'es-ar', 'dua-cm', 'en-ws', 'nmg-cm', 'ca-es', 'rwk', 'uz-cyrl', 'gu', 'bs-cyrl-ba', 'en-in', 'ksb', 'ar-tn',
    'sr-latn-me', 'ar-qa', 'tzm', 'ms-latn-my', 'ts-za', 'fr-fr', 'es', 'fr-mr', 'ko-kp', 'ja-jp', 'st-za', 'fur',
    'fr-bl', 'ca-ad', 'ro-ro', 'vai-vaii', 'ar', 'fr-sn', 'as-in', 'de-at', 'bm-latn-ml', 'fr-mu', 'en-mu',
    'zh-hans-mo', 'en-tt', 'da-dk', 'ka', 'sah-ru', 'sv-ax', 'fr-ml', 'nn-no', 'nl-cw', 'en-sx', 'ak-gh', 'kea-cv',
    'ar-dz', 'zu-za', 'uz-arab', 'ckb-latn', 'tzm-latn', 'es-mx', 'in', 'fr-ne', 'so-dj', 'qu-bo', 'es-gt', 'lu-cd',
    'zh-tw', 'en-sg', 'pa-arab-pk', 'xh', 've', 'mgo', 'en-ai', 'fr-ch', 'fr-ht', 'tr-tr', 'kkj-cm', 'kl', 'agq', 'hy',
    'ast-es', 'swc-cd', 'se-no', 'ar-eh', 'es-py', 'luy', 'ewo', 'ff-mr', 'zgh', 'bem', 'nl-aw', 'bez-tz', 'en-nu',
    'ru-ua', 'km-kh', 'de-be', 'en-zw', 'es-cl', 'kl-gl', 'ar-kw', 'ksf-cm', 'bg', 'yi-001', 'luo-ke', 'en-as', 'fr-cg',
    'ta', 'nr', 'sr-cyrl-ba', 'en-er', 'de-li', 'hu-hu', 'ks-arab-in', 'shi-latn', 'fa-ir', 'en-ke', 'ks-arab',
    'vai-latn-lr', 'asa', 'jmc', 'vai-vaii-lr', 'ii', 'et-ee', 'en-bw', 'dsb', 'ln', 'nl-nl', 'ar-km', 'az', 'vai',
    'ru-kg', 'dsb-de', 'sl-si', 'lb', 'ksh-de', 'nus', 'en-sc', 'fr-gn', 'ar-ye', 'fr-cf', 'haw-us', 'fil-ph', 'agq-cm',
    'khq', 'en-vu', 'en-tc', 'en-ug', 'nd', 'en', 'en-gb', 'brx-in', 'sn', 'yo-bj', 'ar-sy', 'tn-za', 'de-lu',
    'mn-cyrl', 'bm', 'en-cc', 'kk-cyrl-kz', 'seh', 'fy-nl', 'hr-hr', 'ckb', 'smn', 'fr-bf', 'fr-tn', 'fr-yt', 'ga-ie',
    'ka-ge', 'ha-latn-ne', 'en-150', 'bg-bg', 'ar-ps', 'it-it', 'nyn-ug', 'nn', 'gd', 'sw-ke', 'br-fr', 'fr-mc',
    'sn-zw', 'xog', 'fa', 'fr-vu', 'guz-ke', 'da', 'hi-in', 'kok', 'kam', 'yav-cm', 'mg-mg', 'sv-fi', 'ca-es-valencia',
    'ps', 'sr', 'qu', 'ar-001', 'en-sl', 'sr-latn-ba', 'es-ph', 'dua', 'ki', 'bas-cm', 'ta-sg', 'aa-et'
]

for lang in _langs:
    locals()["angular_locale_{0}".format(lang).replace("-", "_")] = Resource(
        library,
        "i18n/angular-locale_{0}.js".format(lang)
    )
