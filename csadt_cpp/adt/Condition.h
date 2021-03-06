#ifndef __CONDITION_H__
#define __CONDITION_H__

#include <vector>
#include <iostream>
#include <string>

#include "Instance.h"

using namespace std;

class Condition
{
public:
	Condition();
	Condition(const Condition& c);
	Condition(const unsigned& myValue, const string& myComparison, const unsigned& myIndex);
	Condition(const unsigned& myValue, const string& myComparison, const unsigned& myIndex, const bool& myNotFlag);

	unsigned getValue() const;
	void setValue(const unsigned& v);

	string getComparison() const;
	void setComparison(const string& c);

	// This corresponds to which field is being compared
	// index: 1 === eFullName
	unsigned getIndex() const;
	void setIndex(const unsigned& i);

	bool getNotFlag() const;
	void setNotFlag(const bool& n);
	bool considerNotFlag(const bool& c) const;
	string toString() const;

	bool evaluate(const Instance& instance) const;

	Condition& operator=(const Condition& c);

	bool operator==(const Condition& c);

private:
	unsigned value;
	string comparison;
	unsigned index;
	bool notFlag;
};

ostream& operator<<(ostream& out, const Condition& i);

enum ComparisonIndices
{
	eLessThan = 0,
	eGreatherThan,
	eEqualTo,
	eLessThanOrEqual,
	eGreaterThanOrEqual,
	eNumValidComparisons
};

static string sValidComparisons[eNumValidComparisons] =
{
	"<",
	">",
	"==",
	"<=",
	">="
};

#endif
