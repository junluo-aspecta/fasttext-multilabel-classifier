# coding=utf-8
# Copyright 2019 YAM AI Machinery Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import getopt
import sys
from settings import LEARNING_RATE, WORD_N_GRAMS, EPOCH, LOSS
from fasttext import train_supervised


def gen_model_file(trainfile, modelfile, wordNgrams=WORD_N_GRAMS, lr=LEARNING_RATE, epoch=EPOCH, loss=LOSS):
    print('Input training file: {}'.format(trainfile))
    print('Output model file: {}'.format(modelfile))
    print('Learning rate: {}'.format(lr))
    print('Word n-grams: {}'.format(wordNgrams))
    print('Epoch: {}'.format(epoch))
    print('Loss: {}'.format(loss))
    try:
        model = train_supervised(
            trainfile, wordNgrams=wordNgrams, lr=lr, epoch=epoch, loss=loss)
        model.save_model(modelfile)
    except Exception as e:
        raise Exception(
            'Failed to perform supervised training using file {}: {}'.format(trainfile, e))


def main(argv):
    try:
        opts, _ = getopt.getopt(argv[1:], 'i:o:')
    except Exception as e:
        usage(argv[0])
    trainfile = None
    modelfile = None
    try:
        for opt, arg in opts:
            if opt == '-i':
                trainfile = arg
                continue
            if opt == '-o':
                modelfile = arg
                continue
    except Exception as e:
        usage(argv[0], e)
    if not trainfile:
        usage(argv[0], 'Missing train_file')
    if not modelfile:
        usage(argv[0], 'Missing model_file')

    try:
        gen_model_file(trainfile, modelfile)
    except Exception as e:
        print('Error: {}'.format(e), file=sys.stderr)


def usage(progname, e=None):
    print('Usage: {} -i train_file -o model_file'.format(progname), file=sys.stderr)
    if e:
        print(e, file=sys.stderr)
    sys.exit(1)


if __name__ == '__main__':
    main(sys.argv)
