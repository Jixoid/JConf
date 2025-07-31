#
#  This file is part of JConf.
#
#  This file is licensed under the GNU Lesser General Public License version 3 (LGPLv3).
#
#  You should have received a copy of GNU Lesser General Public License
#  along with JConf. If not, see <https://www.gnu.org/licenses/>.
#
#  Copyright (c) 2025 by Kadir Aydın.
#




include Make.inc



Build:
	@echo "♦️ Build"
	@echo


	@$(MAKE) -C Pkgs  Build
	@echo

	@echo "Successfuly Compiled!"
	@echo


Clean:
	@echo "♦️ Clean"
	@echo


	@$(MAKE) -C Pkgs  Clean
	@echo


ReBuild: Clean Build


RPM: Build
	@echo "♦️ RPM Build"
	@echo

  # RPM
	@rm -rf @RPM
	@mkdir -p @RPM/{BUILD,RPMS,SOURCES,SPECS,SRPMS}

  # JConf
	@mkdir -p @RPM/SOURCES/jconf/{Inc,Lib}

	@cp Pkgs/lib.qaos.jconf.dev/Inc/*   @RPM/SOURCES/jconf/Inc
	@cp Pkgs/lib.qaos.jconf/@Out/Lib/*  @RPM/SOURCES/jconf/Lib

	@tar czf @RPM/SOURCES/jconf.tar.gz  -C @RPM/SOURCES jconf

	@cp jconf.spec @RPM/SPECS


  # Create
	@rpmbuild --quiet -ba @RPM/SPECS/jconf.spec --define "_topdir $$(pwd)/@RPM"


	@echo "Successfuly Packed!"
	@echo

