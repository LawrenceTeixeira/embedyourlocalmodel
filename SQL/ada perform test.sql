--- CONTENT SEARCH
--- Same as for TITLE sample, but on CONTENT

create table #trab ( linha varchar( 200) null )

insert into #trab (linha) values ('Model: text-embedding-ada-002')

declare @v nvarchar(max)
select @v = content_vector from dbo.wikipedia_articles_embeddings where title = 'Microsoft'

insert into #trab (linha) values ('')
insert into #trab (linha) values ('Search with 1 cluster')

insert into #trab (linha)
select w.title from 
(select top (10) id, title, text, dot_product
from [$vector].find_similar$wikipedia_articles_embeddings$content_vector(@v, 1, 0.25) 
order by dot_product desc) w
order by w.title
go

declare @v nvarchar(max)
select @v = content_vector from dbo.wikipedia_articles_embeddings where title = 'Microsoft'

insert into #trab (linha) values ('')
insert into #trab (linha) values ('Search with 4 clusters')

insert into #trab (linha)
select w.title from 
(select top (10) id, title, text, dot_product
from [$vector].find_similar$wikipedia_articles_embeddings$content_vector(@v, 4, 0.25) 
order by dot_product desc) w
order by w.title
go

declare @v nvarchar(max)
select @v = content_vector from dbo.wikipedia_articles_embeddings where title = 'Microsoft'

insert into #trab (linha) values ('')
insert into #trab (linha) values ('Search with 8 clusters')

insert into #trab (linha)
select w.title from 
(select top (10) id, title, text, dot_product
from [$vector].find_similar$wikipedia_articles_embeddings$content_vector(@v, 8, 0.25) 
order by dot_product desc) w
order by w.title
go

declare @v nvarchar(max)
select @v = content_vector from dbo.wikipedia_articles_embeddings where title = 'Microsoft'

insert into #trab (linha) values ('')
insert into #trab (linha) values ('Search with 16 clusters')

insert into #trab (linha)
select w.title from 
(select top (10) id, title, text, dot_product
from [$vector].find_similar$wikipedia_articles_embeddings$content_vector(@v, 16, 0.25) 
order by dot_product desc) w
order by w.title
go

select * from #trab

drop table #trab
