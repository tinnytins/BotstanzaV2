import json


class Configuration(object):

    config_serialisation_format = '{"BannedWordsPathModerate":"{0}","BannedWordsPathSevere":"{1}","BotToken":"{2}","FilterExcludedChannels":"{3}","IntroductionChannel":"{4}","MuteRole":"{5}","Prefix":"{6}","ProfanityFilterEnabled":"{7}","ReportChannel":"{8}","RPSEnabled":"{9}","SelfiesChannel":"{10}","StaffChannel":"{11}","SuggestionsChannel":"{12}","SuggestionsEnabled":"{13}"}'

    # general
    bot_token = ""
    staff_channel = ""
    mute_role = ""
    prefix = ""
    report_channel = ""
    selfies_channel = ""
    intro_channel = ""

    # rps
    rps_enabled = ""

    # Profanity filter
    filter_enabled = ""
    filter_words_path_severe = ""
    filter_words_path_moderate = ""
    filter_excluded_channels = []

    # suggestions
    suggestions_enabled = ""
    suggestions_channel = ""

    @staticmethod
    def __init__():
        conf = json.load(open("./data/conf.json", "r"))
        Configuration.bot_token = str(conf["BotToken"])
        Configuration.rps_enabled = Configuration.string_to_bool(conf["RPSEnabled"])
        Configuration.filter_enabled = Configuration.string_to_bool(conf["ProfanityFilterEnabled"])
        Configuration.filter_words_path_severe = conf["BannedWordsPathSevere"]
        Configuration.staff_channel = int(conf["StaffChannel"])
        Configuration.suggestions_channel = int(conf["SuggestionsChannel"])
        Configuration.mute_role = int(conf["MuteRole"])
        Configuration.filter_words_path_moderate = str(conf["BannedWordsPathModerate"])
        Configuration.suggestions_enabled =  Configuration.string_to_bool(conf["SuggestionsEnabled"])
        Configuration.prefix = str(conf["Prefix"])
        Configuration.report_channel = int(conf["ReportChannel"])
        Configuration.selfies_channel = int(conf["SelfiesChannel"])
        Configuration.intro_channel = int(conf["IntroductionChannel"])
        Configuration.filter_excluded_channels = str(conf["FilterExcludedChannels"]).split(",")

    @staticmethod
    def string_to_bool(string):
        return str(string).lower() == "true"

    @staticmethod
    def save_config():
        open("./data/conf.json", "w").write(serialize_config())


    def serialize_config():
        return config_serialisation_format.format(Configuration.filter_words_path_moderate,Configuration.filter_words_path_severe,Configuration.bot_token,Configuration.filter_excluded_channels,Configuration.intro_channel,Configuration.mute_role,Configuration.prefix,Configuration.filter_enabled,Configuration.report_channel,Configuration.selfies_channel,Configuration.staff_channel,Configuration.suggestions_channel,Configuration.suggestions_enabled)