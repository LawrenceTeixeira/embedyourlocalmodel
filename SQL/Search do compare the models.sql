--- CONTENT SEARCH
--- Same as for TITLE sample, but on CONTENT

declare @v nvarchar(max)
select @v = content_vector from dbo.wikipedia_articles_embeddings where title = 'Microsoft'
select w.title, w.text from 
(select top (10) id, title, text, dot_product from [$vector].find_similar$wikipedia_articles_embeddings$content_vector(@v, 1, 0.75) 
order by dot_product desc) w order by w.title
go

declare @v nvarchar(max)
select @v = content_vector from dbo.wikipedia_articles_embeddings where title = 'Microsoft'
select w.title, w.text from 
(select top (10) id, title, text, dot_product from [$vector].find_similar$wikipedia_articles_embeddings$content_vector(@v, 50, 0.75) 
order by dot_product desc) w order by w.title
go