############################################################
## Variables:                                              #
##                                                         #
## DEPLOY_TRAVIS ------> 1 para activar releases           #
## USER_TRAVIS --------> usuario de github                 #
## EMAIL_TRAVIS -------> email de github                   #
## MILESTONE_TRAVIS ---> número de milestone               #
## NOMBRE_ZIP ---------> grooving                          #
## RAMA_TRAVIS --------> CI-Integration                    #
## TOKEN_TRAVIS -------> token personal sin encriptar      #
############################################################

language: python

python:
  - 3.6

sudo: required
dist: trusty
addons:
  postgresql: "9.6"

services:
  - postgresql

# env:
# - DJANGO_SETTINGS_MODULE="grooving.settings"

install:
  - pip install -r grooving-server/requirements.txt

before_script:
  - psql -c "create user grooving with password 'e35bdc42'" -U postgres
  - psql -c "create database grooving owner grooving" -U postgres

script:
  - python ./manage.py makemigrations
  - python ./manage.py migrate
#  - python ./decide/manage.py compilemessages
#  - python ./decide/manage.py test ./decide
  - if [[ $TRAVIS_BRANCH == $RAMA_TRAVIS ]] && [[ $DEPLOY_TRAVIS == "1" ]]; then git archive --format zip --output ./$NOMBRE_ZIP.zip $RAMA_TRAVIS; echo "Zip generado correctamente."; fi

    # before_deploy:
    #- git config --local user.name $USER_TRAVIS
    #- git config --local user.email $EMAIL_TRAVIS
    #- export YEAR=`date +"%Y"`  
    #- export GIT_TAG=v$MILESTONE_TRAVIS.0.$TRAVIS_BUILD_NUMBER-$YEAR
    #- git tag -a $GIT_TAG -m "Generated tag from TravisCI build $TRAVIS_BUILD_NUMBER"

deploy:
  provider: releases
  api-key:
    secure: $TOKEN_TRAVIS
  file: "./$NOMBRE_ZIP.zip"
  skip_cleanup: true
  on:
    branch: $RAMA_TRAVIS
    condition: $DEPLOY_TRAVIS = 1
    tags: false

notifications:
  email: false
