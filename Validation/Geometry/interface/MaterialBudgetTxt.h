#ifndef MaterialBudgetTxt_h
#define MaterialBudgetTxt_h 1

#include <fstream>

#include "Validation/Geometry/interface/MaterialBudgetFormat.h"


class MaterialBudgetTxt : public MaterialBudgetFormat
{
 public:
  MaterialBudgetTxt( MaterialBudgetData* data, const std::string& fileName );   
  ~MaterialBudgetTxt() override;

  void fillStartTrack() override;
  void fillPerStep() override;
  void fillEndTrack() override;

 private:
  std::ofstream* theFile;

};

#endif
