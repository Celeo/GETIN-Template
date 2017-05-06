#!/bin/bash
docker run -ti --rm -v `pwd`/client:/srv celeo/yarn:latest bash -c 'cd /srv && yarn && yarn run build'
