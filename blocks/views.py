from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blocks.models import Block
from django import db
from . import api_requests
import datetime

def blocks(request):
    block = api_requests.get_all_blocks()

    for elem in block:
        block_exists = Block.objects.filter(height=elem['height']).count()
        if block_exists == 0:
            q = Block(
                height=int(elem['height']),
                hash=elem['hash'],
                time=datetime.datetime.fromtimestamp(int(elem['timestamp'])),
                miner=elem['miner'],
                transactions=elem['transactionCount'],
            )
            q.save()

    blocks_all = Block.objects.all()[::-1]

    page = request.GET.get('page')
    paginator = Paginator(blocks_all, 50)

    try:
        block = paginator.page(page)
    except PageNotAnInteger:
        block = paginator.page(1)
    except EmptyPage:
        block = paginator.page(paginator.num_pages)

    context = {'blocks': block}
    return render(request,'blocks/blocks.html',context)

def detail_block(request, pk):
    # block = api_requests.get_detail_block(pk)
    context = {'block': Block.objects.get(height=pk)}
    return render(request,'blocks/detail_block.html', context)
