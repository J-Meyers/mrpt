/* +------------------------------------------------------------------------+
   |                     Mobile Robot Programming Toolkit (MRPT)            |
   |                          http://www.mrpt.org/                          |
   |                                                                        |
   | Copyright (c) 2005-2019, Individual contributors, see AUTHORS file     |
   | See: http://www.mrpt.org/Authors - All rights reserved.                |
   | Released under BSD License. See details in http://www.mrpt.org/License |
   +------------------------------------------------------------------------+ */
#pragma once

#include <string>

namespace mrpt::containers
{
/** A case-insensitive comparator class for use within STL containers, etc.
 * \note Credits: https://stackoverflow.com/a/1801913/1631514
 * \note This is the C++11 updated version of mrpt-1.x <mrpt/utils/ci_less.h>
 * \ingroup mrpt_containers_grp
 */
struct ci_less
{
	struct nocase_compare
	{
		bool operator()(const unsigned char& c1, const unsigned char& c2) const
		{
			return tolower(c1) < tolower(c2);
		}
	};
	bool operator()(const std::string& s1, const std::string& s2) const
	{
		return std::lexicographical_compare(
			s1.begin(), s1.end(),  // source range
			s2.begin(), s2.end(),  // dest range
			nocase_compare());  // comparison
	}
};

}  // namespace mrpt::containers
