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



include ../../Make.inc



# Targets

Build: Basis  $(Out)/Package.moq


Basis:
	@mkdir -p $(Out)


Clean:
	@rm -rf $(Out)



# Files

$(Out)/Package.moq: Inc/JConf.h
	@echo "  - 📦️ Packing"

	@rm -f $(Out)/Package.moq
	@tar -cf $(Out)/Package.moq  -C . Package.conf  -C . Inc


