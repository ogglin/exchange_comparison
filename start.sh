#!/bin/bash
ps auxww | grep 'celery' | awk '{print $2}' | xargs kill -9
sleap 3
celery -A exchange_comparison purge --force
sleap 3
celery -A exchange_comparison worker -Q exchanges -B -l WARNING -n exchanges@vp4.ru &
celery -A exchange_comparison worker -Q idex -B -l WARNING -n idex@vp4.ru &
celery -A exchange_comparison worker -Q uniswap -B -l WARNING -n uniswap@vp4.ru &
celery -A exchange_comparison worker -Q kyber -B -l WARNING -n kyber@vp4.ru &
celery -A exchange_comparison worker -Q normal -B -l WARNING -n normal@vp4.ru &

#celery -A exchange_comparison worker -Q hotbit -B -l WARNING -n hotbit@vp4.ru &
#celery -A exchange_comparison worker -Q bancor -B -l WARNING -n bancor@vp4.ru &
#celery -A exchange_comparison worker -Q uniswap_one -B -l WARNING -n uniswap_one@vp4.ru &