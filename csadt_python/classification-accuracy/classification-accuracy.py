import sys
import os
import string
import re
import math
import adt
import adt_infrastructure

SAME = "SAME"
DIFFERENT = "DIFFERENT"

def Usage():
	print "**************************************************"
	print "Usage  : python %s [text (.txt) input file] [text (.txt) input file] [output file prefix]" % sys.argv[0]
	print "Example: python %s testing_data.txt Tree.txt 1" % sys.argv[0]
	print "**************************************************"
	print "Your arguments:", sys.argv

def main():
	if len(sys.argv) != 4:
		Usage()
		return

	training_comparisons_file = sys.argv[1]
	adtree_file = sys.argv[2]
	output_file_prefix = sys.argv[3]

	if os.path.exists(training_comparisons_file) and os.path.exists(adtree_file):
		adtree = adt_infrastructure.ReCreateADTree(adtree_file, adt)

		number_of_matches, number_of_nonmatches, trainingComparisonPairs = adt_infrastructure.BuildComparisonPairsDataStructure(training_comparisons_file)
		outputDatabase = adt.evaluate(trainingComparisonPairs, adtree)

		number_of_matches = float(number_of_matches)
		number_of_nonmatches = float(number_of_nonmatches)

		correct_classifications = 0.0
		incorrect_classifications = 0.0

		number_of_predicted_matches = 0.0
		number_of_predicted_nonmatches = 0.0

		true_positives = 0.0
		true_negatives = 0.0
		false_positives = 0.0
		false_negatives = 0.0
		for combination_pair in outputDatabase.keys():
			# true positives
			if trainingComparisonPairs[combination_pair]["classification"] == SAME and outputDatabase[combination_pair]["classification"] == SAME:
				true_positives = true_positives + 1.0
				correct_classifications = correct_classifications + 1.0
				number_of_predicted_matches = number_of_predicted_matches + 1.0
			# true negatives
			elif trainingComparisonPairs[combination_pair]["classification"] == DIFFERENT and outputDatabase[combination_pair]["classification"] == DIFFERENT:
				true_negatives = true_negatives + 1.0
				correct_classifications = correct_classifications + 1.0
				number_of_predicted_nonmatches = number_of_predicted_nonmatches + 1.0
			else:
				# false positives
				if outputDatabase[combination_pair]["classification"] == SAME:
					#print "False Positive:", outputDatabase[combination_pair]
					false_positives = false_positives + 1.0
					incorrect_classifications = incorrect_classifications + 1.0
					number_of_predicted_matches = number_of_predicted_matches + 1.0
				# false negatives
				elif outputDatabase[combination_pair]["classification"] == DIFFERENT:
					#print "False Negative:", outputDatabase[combination_pair]
					false_negatives = false_negatives + 1.0
					incorrect_classifications = incorrect_classifications + 1.0
					number_of_predicted_nonmatches = number_of_predicted_nonmatches + 1.0
				else:
					print " **************************** THIS SHOULD NEVER HAPPEN"

		# Precision = TruePositives / (TruePositives + FalseNegatives)
		precision_denominator = true_positives + false_negatives
		if precision_denominator == 0:
			print " ### ERROR: Precision could not be calculated because (true_positives + false_negatives) = 0"
			precision_denominator = 0.001
		precision = true_positives / precision_denominator * 100.0

		# Recall = TruePositives / (TruePositives + FalsePositives)
		recall_denominator = true_positives + false_positives
		if recall_denominator == 0:
			print " ### ERROR: Recall could not be calculated because (true_positives + false_positives) = 0"
			recall_denominator = 0.001
		recall = true_positives / recall_denominator * 100.0

		#             (TruePositives + TrueNegatives)
		# Accuracy = --------------------------------------------------------------------
		#             (TruePositives + True Negatives + FalsePositives + FalseNegatives)
		accuracy_denominator = true_positives + true_negatives + false_positives + false_negatives
		if accuracy_denominator == 0:
			print " ### ERROR: Accuracy could not be calculated because (true_positives + true_negatives + false_positives + false_negatives) = 0"
			accuracy_denominator = 0.001
		accuracy = (true_positives + true_negatives) / accuracy_denominator * 100.0

		print ""
		print " Training Data Record-Pairs    : %s" % len(outputDatabase)
		print ""
		print " Number of matches             : %s" % str(int(number_of_matches))
		print " Number of nonmatches          : %s" % str(int(number_of_nonmatches))
		print ""
		print " Number of predicted matches   : %s" % str(int(number_of_predicted_matches))
		print " Number of predicted nonmatches: %s" % str(int(number_of_predicted_nonmatches))
		print ""
		print " True Positives                : %s detected of %s (%.2f%%)" % (str(int(true_positives)), str(int(number_of_matches)), true_positives / number_of_matches * 100.0)
		print " True Negatives                : %s detected of %s (%.2f%%)" % (str(int(true_negatives)), str(int(number_of_nonmatches)), true_negatives / number_of_nonmatches * 100.0)
		print " False Positives               : %s" % str(int(false_positives))
		print " False Negatives               : %s" % str(int(false_negatives))
		print ""
		print " Recall                        : %s%%" % precision
		print " Precision                     : %s%%" % recall
		print " Accuracy                      : %s%%" % accuracy
		print ""

		with open(output_file_prefix + "-Precision.txt", 'w') as f_precision:
			f_precision.write(str(precision))
			f_precision.write("\n")
		with open(output_file_prefix + "-Recall.txt", 'w') as f_recall:
			f_recall.write(str(recall))
			f_recall.write("\n")
		with open(output_file_prefix + "-Accuracy.txt", 'w') as f_accuracy:
			f_accuracy.write(str(accuracy))
			f_accuracy.write("\n")

	else:
		Usage()
		return

if __name__ == "__main__":
	main()
