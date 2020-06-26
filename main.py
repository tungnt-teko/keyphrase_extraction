from wordbook import Wordbook
from textrank import TextRankModel
from extractor import Extractor
from tpr import LDAModel, TopicalPageRank

# extractor = Extractor()

# dataset = 'datasets/data_original_files0-9999'
# wb = Wordbook(folder_path=dataset)
# wb.extract_corpora(extractor)
# wb.set_ignored_words(min_df_count=2, max_df=0.65)

# extractor.stop()

# tr = TextRankModel(min_diff=1e-6, steps=20)
# tr.set_ignored_words(wb.ignored_words)


extractor = Extractor()

dataset = 'datasets/data_original_files0-9999'
wb = Wordbook(folder_path=dataset)
wb.extract_corpora(extractor)
wb.set_ignored_words(min_df_count=2, max_df=0.65)

extractor.stop()

lda_model = LDAModel(wb.corpora)
lda_model.init_model(num_topics=100)

tpr = TopicalPageRank(
    window_size=4,
    damping=0.85,
    min_diff=1e-6,
    steps=25
)
tpr.set_extensions(lda_model=lda_model, ignored_words=wb.ignored_words)
