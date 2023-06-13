SOURCE_METER_PATH = "./Python/SourceMeterPython.exe"

TEMP_DIR_PATH = "_Temp"
RESULTS_DIR = "_SourceMeterMetrics"
STATS_DIR = "_FinalMetrics"
STATS_RESULTS_DIR = "_CorrelationData"

REPO_LINKS = [
    "https://github.com/jackfrued/Python-100-Days",
    "https://github.com/Significant-Gravitas/Auto-GPT",
    "https://github.com/floodsung/Deep-Learning-Papers-Reading-Roadmap",
    "https://github.com/shadowsocks/shadowsocks",
    "https://github.com/microsoft/TaskMatrix",
    "https://github.com/XX-net/XX-Net",
    "https://github.com/PaddlePaddle/PaddleOCR",
    "https://github.com/hpcaitech/ColossalAI",
    "https://github.com/hankcs/HanLP",
    "https://github.com/babysor/MockingBird",
    "https://github.com/ray-project/ray",
    "https://github.com/streamlit/streamlit",
    "https://github.com/tatsu-lab/stanford_alpaca",
    "https://github.com/littlecodersh/ItChat",
    "https://github.com/StevenBlack/hosts",
    "https://github.com/OpenBB-finance/OpenBBTerminal",
    "https://github.com/luong-komorebi/Awesome-Linux-Software",
    "https://github.com/AtsushiSakai/PythonRobotics",
    "https://github.com/plotly/dash",
    "https://github.com/microsoft/recommenders",
    "https://github.com/Delgan/loguru",
    "https://github.com/deepinsight/insightface",
    "https://github.com/openai/baselines",
    "https://github.com/KurtBestor/Hitomi-Downloader",
    "https://github.com/mxrch/GHunt",
    "https://github.com/aleju/imgaug",
    "https://github.com/RunaCapital/awesome-oss-alternatives",
    "https://github.com/lra/mackup",
    "https://github.com/searx/searx",
    "https://github.com/microsoft/unilm",
    "https://github.com/wistbean/learn_python3_spider",
    "https://github.com/zhayujie/chatgpt-on-wechat",
    "https://github.com/PySimpleGUI/PySimpleGUI",
    "https://github.com/donnemartin/awesome-aws",
    "https://github.com/redis/redis-py",
    "https://github.com/GaiZhenbiao/ChuanhuChatGPT",
    "https://github.com/ytisf/theZoo",
    "https://github.com/rougier/scientific-visualization-book",
    "https://github.com/pallets/jinja",
    "https://github.com/PaddlePaddle/PaddleNLP",
    "https://github.com/coursera-dl/coursera-dl",
    "https://github.com/benoitc/gunicorn",
    "https://github.com/seatgeek/fuzzywuzzy",
    "https://github.com/numba/numba",
    "https://github.com/sloria/TextBlob",
    "https://github.com/togethercomputer/OpenChatKit",
    "https://github.com/kedro-org/kedro",
    "https://github.com/injetlee/Python",
    "https://github.com/boto/boto3",
    "https://github.com/deepmind/pysc2",
    "https://github.com/microsoft/fluentui-emoji",
    "https://github.com/gelstudios/gitfiti",
    "https://github.com/dagster-io/dagster",
    "https://github.com/lazyprogrammer/machine_learning_examples",
    "https://github.com/donnemartin/gitsome",
    "https://github.com/facebookresearch/pytorch3d",
    "https://github.com/qubvel/segmentation_models.pytorch",
    "https://github.com/dylanaraps/pywal",
    "https://github.com/tensorlayer/TensorLayer",
    "https://github.com/rossant/awesome-math",
    "https://github.com/catboost/catboost",
    "https://github.com/ajenti/ajenti",
    "https://github.com/hellerve/programming-talks",
    "https://github.com/mlc-ai/mlc-llm",
    "https://github.com/bup/bup",
    "https://github.com/openai/jukebox",
    "https://github.com/neonbjb/tortoise-tts",
    "https://github.com/houtianze/bypy",
    "https://github.com/platformio/platformio-core",
    "https://github.com/axi0mX/ipwndfu",
    "https://github.com/tkipf/gcn",
    "https://github.com/stanfordnlp/stanza",
    "https://github.com/pyeve/eve",
    "https://github.com/googleapis/google-api-python-client",
    "https://github.com/encode/uvicorn",
    "https://github.com/marshmallow-code/marshmallow",
    "https://github.com/vt-vl-lab/3d-photo-inpainting",
    "https://github.com/sktime/sktime",
    "https://github.com/pypa/pipx",
    "https://github.com/scikit-learn-contrib/imbalanced-learn",
    "https://github.com/numenta/nupic",
    "https://github.com/docker/docker-py",
    "https://github.com/mahmoud/boltons",
    "https://github.com/jrnl-org/jrnl",
    "https://github.com/PaddlePaddle/ERNIE",
    "https://github.com/ashawkey/stable-dreamfusion",
    "https://github.com/codertimo/BERT-pytorch",
    "https://github.com/longld/peda",
    "https://github.com/jonaswinkler/paperless-ng",
    "https://github.com/frappe/frappe",
    "https://github.com/facebookresearch/SlowFast",
    "https://github.com/bridgecrewio/checkov",
    "https://github.com/StanGirard/quivr",
    "https://github.com/pyca/cryptography",
    "https://github.com/arc53/DocsGPT",
    "https://github.com/longld/peda",
    "https://github.com/scikit-image/scikit-image",
    "https://github.com/jonaswinkler/paperless-ng",
    "https://github.com/openatx/uiautomator2",
    "https://github.com/NVIDIA/Megatron-LM",
    "https://github.com/bndr/pipreqs",
    "https://github.com/bojone/bert4keras",
    "https://github.com/TheR1D/shell_gpt",
    "https://github.com/Rudrabha/Wav2Lip",
    "https://github.com/r0ysue/r0capture",
    "https://github.com/facebookresearch/dinov2",
    "https://github.com/Ultimaker/Cura",
    "https://github.com/pytransitions/transitions",
    "https://github.com/diafygi/acme-tiny",
    "https://github.com/pylint-dev/pylint",
    "https://github.com/CTFd/CTFd",
    "https://github.com/gaomingqi/Track-Anything",
    "https://github.com/nwojke/deep_sort",
    "https://github.com/vyperlang/vyper",
    "https://github.com/pypa/virtualenv",
    "https://github.com/instillai/deep-learning-roadmap",
    "https://github.com/hunshcn/gh-proxy",
    "https://github.com/vitalik/django-ninja",
    "https://github.com/huangsam/ultimate-python",
    "https://github.com/cookiecutter-flask/cookiecutter-flask",
    "https://github.com/PyImageSearch/imutils",
    "https://github.com/mozillazg/python-pinyin",
    "https://github.com/jaungiers/LSTM-Neural-Network-for-Time-Series-Prediction",
    "https://github.com/skywind3000/ECDICT",
    "https://github.com/ethereum/web3.py",
    "https://github.com/MaartenGr/BERTopic",
    "https://github.com/andresriancho/w3af",
    "https://github.com/internetarchive/openlibrary",
    "https://github.com/crytic/slither",
    "https://github.com/aws-samples/aws-cdk-examples",
    "https://github.com/python-jsonschema/jsonschema",
    "https://github.com/victoresque/pytorch-template",
    "https://github.com/ticarpi/jwt_tool",
    "https://github.com/qilingframework/qiling",
    "https://github.com/zauberzeug/nicegui",
    "https://github.com/DistrictDataLabs/yellowbrick",
    "https://github.com/pwr-Solaar/Solaar",
    "https://github.com/DropsDevopsOrg/ECommerceCrawlers",
    "https://github.com/google/tf-quant-finance",
    "https://github.com/pythonprofilers/memory_profiler",
    "https://github.com/fastmonkeys/stellar",
    "https://github.com/EvanLi/Github-Ranking",
    "https://github.com/astropy/astropy",
    "https://github.com/lark-parser/lark",
    "https://github.com/arsenetar/dupeguru",
    "https://github.com/Layout-Parser/layout-parser",
    "https://github.com/twopirllc/pandas-ta",
    "https://github.com/python-openxml/python-docx",
    "https://github.com/hacs/integration",
    "https://github.com/python/typeshed",
    "https://github.com/aiogram/aiogram",
    "https://github.com/biopython/biopython",
    "https://github.com/bisguzar/twitter-scraper",
    "https://github.com/yandex/YaLM-100B",
    "https://github.com/nv-tlabs/GET3D",
    "https://github.com/django-haystack/django-haystack",
    "https://github.com/OpenShot/openshot-qt",
    "https://github.com/LyleMi/Learn-Web-Hacking",
    "https://github.com/gaogaotiantian/viztracer",
    "https://github.com/peterbrittain/asciimatics",
    "https://github.com/attardi/wikiextractor",
    "https://github.com/ifzhang/ByteTrack",
    "https://github.com/meetps/pytorch-semseg",
    "https://github.com/pytorch/text",
    "https://github.com/yihong0618/xiaogpt",
    "https://github.com/davidteather/TikTok-Api",
    "https://github.com/minimaxir/gpt-2-simple",
    "https://github.com/flasgger/flasgger",
    "https://github.com/confluentinc/confluent-kafka-python",
    "https://github.com/google/model_search",
    "https://github.com/wzpan/wukong-robot",
    "https://github.com/nwojke/deep_sort",
    "https://github.com/idealo/imagededup",
    "https://github.com/vyperlang/vyper",
    "https://github.com/coleifer/huey",
    "https://github.com/androguard/androguard",
    "https://github.com/hunshcn/gh-proxy",
    "https://github.com/vitalik/django-ninja",
    "https://github.com/ermaozi/get_subscribe",
    "https://github.com/RsaCtfTool/RsaCtfTool",
    "https://github.com/huangsam/ultimate-python",
    "https://github.com/cookiecutter-flask/cookiecutter-flask",
    "https://github.com/fizyr/keras-retinanet",
    "https://github.com/mozillazg/python-pinyin",
    "https://github.com/listen1/listen1",
    "https://github.com/qubvel/segmentation_models",
    "https://github.com/skywind3000/ECDICT",
    "https://github.com/spec-first/connexion",
    "https://github.com/online-ml/river",
    "https://github.com/STVIR/pysot",
    "https://github.com/andresriancho/w3af",
    "https://github.com/shibing624/pycorrector",
    "https://github.com/Guake/guake",
    "https://github.com/tensortrade-org/tensortrade",
    "https://github.com/facebookresearch/xformers",
    "https://github.com/python-jsonschema/jsonschema",
    "https://github.com/tony9402/baekjoon",
    "https://github.com/nsarrazin/serge",
    "https://github.com/Project-MONAI/MONAI",
    "https://github.com/qtile/qtile",
    "https://github.com/carltongibson/django-filter",
    "https://github.com/DistrictDataLabs/yellowbrick",
    "https://github.com/gitpython-developers/GitPython",
    "https://github.com/elastic/elasticsearch-py",
    "https://github.com/derrod/legendary",
    "https://github.com/Netflix/dispatch",
    "https://github.com/DropsDevopsOrg/ECommerceCrawlers",
    "https://github.com/microsoft/BioGPT",
    "https://github.com/pywebio/PyWebIO",
    "https://github.com/google/tf-quant-finance",
    "https://github.com/EvanLi/Github-Ranking",
    "https://github.com/zedr/clean-code-python",
    "https://github.com/anudeepND/whitelist",
    "https://github.com/lark-parser/lark",
    "https://github.com/jina-ai/discoart",
    "https://github.com/quantumlib/Cirq",
    "https://github.com/aaPanel/BaoTa",
    "https://github.com/tmux-python/tmuxp",
    "https://github.com/spulec/freezegun",
    "https://github.com/kernc/backtesting.py",
    "https://github.com/Layout-Parser/layout-parser",
    "https://github.com/lepture/authlib",
    "https://github.com/twopirllc/pandas-ta",
    "https://github.com/layumi/Person_reID_baseline_pytorch",
    "https://github.com/hacs/integration",
    "https://github.com/gd3kr/BlenderGPT",
    "https://github.com/KingOfBugbounty/KingOfBugBountyTips",
    "https://github.com/bmaltais/kohya_ss",
    "https://github.com/WeblateOrg/weblate",
    "https://github.com/tinyvision/DAMO-YOLO",
    "https://github.com/Mebus/cupp",
    "https://github.com/Wookai/paper-tips-and-tricks",
    "https://github.com/nv-tlabs/GET3D",
    "https://github.com/NVlabs/stylegan2-ada-pytorch",
    "https://github.com/InsaneLife/ChineseNLPCorpus",
    "https://github.com/TarrySingh/Artificial-Intelligence-Deep-Learning-Machine-Learning-Tutorials",
    "https://github.com/facebookresearch/dlrm",
    "https://github.com/urllib3/urllib3",
    "https://github.com/karfly/chatgpt_telegram_bot",
    "https://github.com/miguelgrinberg/python-socketio",
    "https://github.com/facundoolano/software-papers",
    "https://github.com/gaogaotiantian/viztracer",
    "https://github.com/tensorflow/hub",
    "https://github.com/0xHJK/music-dl",
    "https://github.com/peterbrittain/asciimatics",
    "https://github.com/attardi/wikiextractor",
    "https://github.com/yihong0618/GitHubPoster",
    "https://github.com/chuyangliu/snake",
    "https://github.com/ml-jku/hopfield-layers",
    "https://github.com/kerrickstaley/genanki",
    "https://github.com/dask/distributed",
    "https://github.com/daleroberts/itermplot",
    "https://github.com/alibaba/EasyCV",
    "https://github.com/microsoft/DirectML",
    "https://github.com/simple-salesforce/simple-salesforce",
    "https://github.com/nithinmurali/pygsheets",
    "https://github.com/fox-it/BloodHound.py",
    "https://github.com/microsoft/NeuronBlocks",
    "https://github.com/pypa/twine",
    "https://github.com/idiap/fast-transformers",
    "https://github.com/m4ll0k/SecretFinder",
    "https://github.com/hyperledger/sawtooth-core",
    "https://github.com/faucetsdn/ryu",
    "https://github.com/opendilab/PPOxFamily",
    "https://github.com/promptslab/Awesome-Prompt-Engineering",
    "https://github.com/patrickloeber/pytorchTutorial",
    "https://github.com/XiphosResearch/exploits",
    "https://github.com/agconti/cookiecutter-django-rest",
    "https://github.com/apple/ml-hypersim",
    "https://github.com/zengyh1900/Awesome-Image-Inpainting",
    "https://github.com/erikrose/blessings",
    "https://github.com/wummel/linkchecker",
    "https://github.com/jet-admin/jet-bridge",
    "https://github.com/78778443/QingScan",
    "https://github.com/quantumlib/OpenFermion",
    "https://github.com/pathak22/noreward-rl",
    "https://github.com/hatRiot/zarp",
    "https://github.com/python/pythondotorg",
    "https://github.com/PrithivirajDamodaran/Gramformer",
    "https://github.com/richardkiss/pycoin",
    "https://github.com/un33k/python-slugify",
    "https://github.com/miguelgrinberg/flask-video-streaming",
    "https://github.com/aio-libs/aiopg",
    "https://github.com/dfm/emcee",
    "https://github.com/nosarthur/gita",
    "https://github.com/kivy/pyjnius",
    "https://github.com/isl-org/Open3D-ML",
    "https://github.com/pytorch/hub",
    "https://github.com/swapagarwal/JARVIS-on-Messenger",
    "https://github.com/pupil-labs/pupil",
    "https://github.com/EleutherAI/lm-evaluation-harness",
    "https://github.com/boto/botocore",
    "https://github.com/scanapi/scanapi",
    "https://github.com/decompiler-explorer/decompiler-explorer",
    "https://github.com/ukdtom/WebTools.bundle",
    "https://github.com/microsoft/GLIP",
    "https://github.com/sebastien/cuisine",
    "https://github.com/649/Memcrashed-DDoS-Exploit",
    "https://github.com/slgobinath/SafeEyes",
    "https://github.com/imageio/imageio",
    "https://github.com/explosion/spacy-transformers",
    "https://github.com/cknd/stackprinter",
    "https://github.com/GlasgowEmbedded/glasgow",
    "https://github.com/bhavsec/reconspider",
    "https://github.com/Netflix/lemur",
    "https://github.com/Akegarasu/lora-scripts",
    "https://github.com/requests/requests-oauthlib",
    "https://github.com/kroitor/asciichart",
    "https://github.com/vulnersCom/getsploit",
    "https://github.com/mrlt8/docker-wyze-bridge",
    "https://github.com/google/spatial-media",
    "https://github.com/brndnmtthws/thetagang",
    "https://github.com/custom-components/ble_monitor",
    "https://github.com/Robot-Will/Stino",
    "https://github.com/borgbase/vorta",
    "https://github.com/django-notifications/django-notifications",
    "https://github.com/ianzhao05/textshot",
    "https://github.com/srsudar/eg",
    "https://github.com/LlmKira/Openaibot",
    "https://github.com/mbr/flask-bootstrap",
    "https://github.com/nateshmbhat/pyttsx3",
    "https://github.com/Delta-ML/delta",
    "https://github.com/ckiplab/ckiptagger",
    "https://github.com/karlicoss/promnesia",
    "https://github.com/pyouroboros/ouroboros",
    "https://github.com/google/android-emulator-container-scripts",
    "https://github.com/volatilityfoundation/volatility3",
    "https://github.com/joelibaceta/video-to-ascii",
    "https://github.com/kivy/buildozer",
    "https://github.com/gtalarico/django-vue-template",
    "https://github.com/fossasia/open-event-scripts",
    "https://github.com/vkbo/novelWriter",
    "https://github.com/omry/omegaconf",
    "https://github.com/salu133445/musegan",
    "https://github.com/dilshod/xlsx2csv",
    "https://github.com/reviewboard/reviewboard",
    "https://github.com/sdv-dev/SDV",
    "https://github.com/facebookincubator/Bowler",
    "https://github.com/Hironsan/anago",
    "https://github.com/graphite-project/carbon",
    "https://github.com/cisagov/Malcolm",
    "https://github.com/pythonarcade/arcade",
    "https://github.com/axcore/tartube",
    "https://github.com/kraanzu/dooit",
    "https://github.com/arxiv-vanity/arxiv-vanity",
    "https://github.com/secretflow/secretflow",
    "https://github.com/natethegreate/hent-AI",
    "https://github.com/nficano/python-lambda",
    "https://github.com/young-geng/EasyLM",
    "https://github.com/pyfa-org/Pyfa",
    "https://github.com/fox-it/BloodHound.py",
    "https://github.com/blacktwin/JBOPS",
    "https://github.com/anymail/django-anymail",
    "https://github.com/lucidrains/lion-pytorch",
    "https://github.com/CodeXBotz/File-Sharing-Bot",
    "https://github.com/ShreyaR/guardrails",
    "https://github.com/agronholm/sqlacodegen",
    "https://github.com/dj-stripe/dj-stripe",
    "https://github.com/realpython/flask-boilerplate",
    "https://github.com/OpenGVLab/InternImage",
    "https://github.com/LinuxCNC/linuxcnc",
    "https://github.com/GFW-knocker/gfw_resist_tls_proxy",
    "https://github.com/arviz-devs/arviz",
    "https://github.com/openstack/openstack-ansible",
    "https://github.com/ddgth/cf2dns",
    "https://github.com/alkaline-ml/pmdarima",
    "https://github.com/iryna-kondr/scikit-llm",
    "https://github.com/adobe-research/custom-diffusion",
    "https://github.com/selwin/python-user-agents",
    "https://github.com/python-control/python-control",
    "https://github.com/celery/django-celery-beat",
    "https://github.com/PrithivirajDamodaran/Gramformer",
    "https://github.com/zero-to-mastery/start-here-guidelines",
    "https://github.com/dongrixinyu/JioNLP",
    "https://github.com/wnma3mz/wechat_articles_spider",
    "https://github.com/Komodo/KomodoEdit",
    "https://github.com/Drakkar-Software/OctoBot",
    "https://github.com/stav121/i3wm-themer",
    "https://github.com/avgupta456/github-trends",
    "https://github.com/boston-dynamics/spot-sdk",
    "https://github.com/dateutil/dateutil",
    "https://github.com/Shougo/denite.nvim",
    "https://github.com/caj2pdf/caj2pdf",
    "https://github.com/Breakthrough/PySceneDetect",
    "https://github.com/openstenoproject/plover",
    "https://github.com/ross/requests-futures",
    "https://github.com/ToxicFrog/Ligaturizer",
    "https://github.com/qubvel/efficientnet",
    "https://github.com/django/daphne",
    "https://github.com/SeanNaren/deepspeech.pytorch",
    "https://github.com/DLR-RM/BlenderProc",
    "https://github.com/MasoniteFramework/masonite",
    "https://github.com/mirumee/ariadne",
    "https://github.com/zhanghang1989/PyTorch-Encoding",
    "https://github.com/opulo-inc/lumenpnp",
    "https://github.com/Yggdroot/LeaderF",
    "https://github.com/THUDM/GLM",
    "https://github.com/zhaoolee/ins",
    "https://github.com/heucoder/dimensionality_reduction_alo_codes",
    "https://github.com/robusta-dev/robusta",
    "https://github.com/tensorflow/tfx",
    "https://github.com/jliljebl/flowblade",
    "https://github.com/edc/bass",
    "https://github.com/pydata/numexpr",
    "https://github.com/argosopentech/argos-translate",
    "https://github.com/sqlalchemy/alembic",
    "https://github.com/facebookresearch/SentEval",
    "https://github.com/jamiemcg/Remarkable",
    "https://github.com/Kapeli/Dash-User-Contributions",
    "https://github.com/OFA-Sys/OFA",
    "https://github.com/pndurette/gTTS",
    "https://github.com/sabnzbd/sabnzbd",
    "https://github.com/open-mmlab/mmdeploy",
    "https://github.com/deepmind/mctx",
    "https://github.com/tobgu/pyrsistent",
    "https://github.com/PyFilesystem/pyfilesystem2",
    "https://github.com/mpoon/gpt-repository-loader",
    "https://github.com/quenhus/uBlock-Origin-dev-filter",
    "https://github.com/Suor/django-cacheops",
    "https://github.com/Daniil-Osokin/lightweight-human-pose-estimation.pytorch",
    "https://github.com/aws/sagemaker-python-sdk",
    "https://github.com/myusuf3/delorean",
    "https://github.com/SheffieldML/GPy",
    "https://github.com/python-restx/flask-restx",
    "https://github.com/salesforce/policy_sentry",
    "https://github.com/microsoft/Deep3DFaceReconstruction",
    "https://github.com/dbcli/litecli",
    "https://github.com/fxia22/pointnet.pytorch",
    "https://github.com/jmespath/jmespath.py",
    "https://github.com/GoogleCloudPlatform/PerfKitBenchmarker",
    "https://github.com/liquidctl/liquidctl",
    "https://github.com/GNS3/gns3-gui",
    "https://github.com/Farama-Foundation/Minigrid",
    "https://github.com/sirfz/tesserocr",
    "https://github.com/RMPR/atbswp",
    "https://github.com/PostmonAPI/postmon",
    "https://github.com/scivision/PyLivestream",
    "https://github.com/django-haystack/pysolr",
    "https://github.com/ApeWorX/ape",
    "https://github.com/rsinger86/drf-flex-fields",
    "https://github.com/google-research/nasbench",
    "https://github.com/mit-han-lab/torchquantum",
    "https://github.com/frescobaldi/frescobaldi",
    "https://github.com/vas3k/vas3k.club",
    "https://github.com/zhuifengshen/xmind2testcase",
    "https://github.com/openai/deeptype",
    "https://github.com/nccgroup/fuzzowski",
    "https://github.com/nasa/apod-api",
    "https://github.com/texturedesign/texturize",
    "https://github.com/python-discord/site",
    "https://github.com/ShichenXie/scorecardpy",
    "https://github.com/artetxem/vecmap",
    "https://github.com/ansible-collections/community.general",
    "https://github.com/tomas789/kitti2bag",
    "https://github.com/aresdevo/animaide",
    "https://github.com/OpenMined/PyGrid-deprecated---see-PySyft-",
    "https://github.com/Trinkle23897/tuixue.online-visa",
    "https://github.com/DisnakeDev/disnake",
    "https://github.com/Squarespace/datasheets",
    "https://github.com/declare-lab/tango",
    "https://github.com/openai/automated-interpretability",
    "https://github.com/SectorLabs/django-postgres-extra",
    "https://github.com/alpacahq/example-hftish",
    "https://github.com/BioPandas/biopandas",
    "https://github.com/WuJunde/MedSegDiff",
    "https://github.com/caoqianming/django-vue-admin",
    "https://github.com/Mathics3/mathics-core",
    "https://github.com/Blizzard/s2protocol",
    "https://github.com/google-research/lasertagger",
    "https://github.com/SickGear/SickGear",
    "https://github.com/platelminto/chatgpt-conversation",
    "https://github.com/gwang-kim/DiffusionCLIP",
    "https://github.com/alpha-miner/Finance-Python",
    "https://github.com/symphonly/figaro",
    "https://github.com/executablebooks/MyST-Parser",
    "https://github.com/Sniper970119/dianping_spider",
    "https://github.com/SAML-Toolkits/python3-saml",
    "https://github.com/denBot/yasb",
    "https://github.com/FirmWire/FirmWire",
    "https://github.com/tomas789/kitti2bag",
    "https://github.com/allure-framework/allure-python",
    "https://github.com/aresdevo/animaide",
    "https://github.com/Squarespace/datasheets",
    "https://github.com/mcfunley/pugsql",
    "https://github.com/SectorLabs/django-postgres-extra",
    "https://github.com/webosose/build-webos",
    "https://github.com/cleanlab/cleanvision",
    "https://github.com/rspeer/wordfreq",
    "https://github.com/BLKSerene/Wordless",
    "https://github.com/TinyDataML/Tiny3D",
    "https://github.com/WikiTeam/wikiteam",
    "https://github.com/greatscottgadgets/Facedancer",
    "https://github.com/FormerLurker/Octolapse",
    "https://github.com/arvkevi/kneed",
    "https://github.com/yxlllc/DDSP-SVC",
    "https://github.com/gusye1234/LightGCN-PyTorch",
    "https://github.com/alegonz/baikal",
    "https://github.com/freqtrade/technical",
    "https://github.com/music-assistant/hass-music-assistant",
    "https://github.com/Yelp/bravado",

    ]