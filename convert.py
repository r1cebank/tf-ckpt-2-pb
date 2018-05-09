import tensorflow as tf
from argparse import ArgumentParser

def main():
    parser = ArgumentParser()
    parser.add_argument('--checkpoint', type=str,
                        dest='checkpoint',
                        help='dir or .ckpt file to load checkpoint from',
                        metavar='CHECKPOINT', required=True)
    parser.add_argument('--model', type=str,
                        dest='model',
                        help='.meta for your model',
                        metavar='MODEL', required=True)
    parser.add_argument('--out-path', type=str,
                        dest='out_path',
                        help='model output directory',
                        metavar='MODEL_OUT', required=True)
    opts = parser.parse_args()
    tf.reset_default_graph()
    saver = tf.train.import_meta_graph(opts.model)
    builder = tf.saved_model.builder.SavedModelBuilder(opts.out_path)
    with tf.Session() as sess:
        # Restore variables from disk.
        saver.restore(sess, opts.checkpoint)
        print("Model restored.")
        builder.add_meta_graph_and_variables(sess,
                                       ['tfckpt2pb'],
                                       strip_default_attrs=False)
        builder.save()

if __name__ == '__main__':
    main()
