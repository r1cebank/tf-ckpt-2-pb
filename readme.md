# tensorflow ckpt to pb

Wrote a simple cli application that will convert saved tensorflow checkpoint to pb savedModel.

Reason behind this is sometimes I am writing tensorflow.js programs and some of the models saved by checkpoint needs to be converted to [SavedModel](https://www.tensorflow.org/programmers_guide/saved_model), nothing fancy just a simple tool i use for myself

Usage:

```
python convert.py --checkpoint XX --model XX --out-path ./export
```

### --checkpoint
The file path of your checkpoint
### --model
The exported [MetaGraph](https://www.tensorflow.org/api_guides/python/meta_graph)
### --out
The output directory, needs to be none existant

The outputed saved model will have the tag `tfckpt2pb`
