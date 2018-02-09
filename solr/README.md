package com.github.tteofili.looseen.dl4j;

import org.apache.lucene.index.IndexReader;
import org.apache.lucene.search.similarities.BasicStats;
import org.apache.lucene.search.similarities.SimilarityBase;
import org.deeplearning4j.nn.multilayer.MultiLayerNetwork;
import org.nd4j.linalg.api.buffer.FloatBuffer;
import org.nd4j.linalg.api.ndarray.INDArray;
import org.nd4j.linalg.factory.Nd4j;

/**
 * A simple {@link Similarity} based on a neural network which takes index, term and frequency stats as inputs,
 * generating the score as output.
 */
public class NNFreqScoringSimilarity extends SimilarityBase {

  private final MultiLayerNetwork network;

  public NNFreqScoringSimilarity(MultiLayerNetwork network) {
    this.network = network;
  }

  @Override
  protected float score(BasicStats stats, float freq, float docLen) {
    int inputSize = 8;

    float[] doubles = new float[inputSize];
    doubles[0] = stats.getAvgFieldLength();
    doubles[1] = stats.getBoost();
    doubles[2] = (float) stats.getDocFreq();
    doubles[3] = (float) stats.getNumberOfDocuments();
    doubles[4] = (float) stats.getNumberOfFieldTokens();
    doubles[5] = (float) stats.getTotalTermFreq();
    doubles[6] = freq;
    doubles[7] = docLen;

    INDArray input = Nd4j.create(new FloatBuffer(doubles), new int[] {1, inputSize});
    input.divi(input.ameanNumber());

    float v = network.feedForward(input, true).get(network.getnLayers()).maxNumber().floatValue();
    return Float.isFinite(v) ? v : 0;
  }

  @Override
  public String toString() {
    return network.toString();
  }
}
 @dougc333
  
            
 
Write
