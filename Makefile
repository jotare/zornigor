# Zornigor
API_MAKE = make -C api/
WEB_MAKE = make -C frontend/web/


api-install:
	${API_MAKE} install

web-install:
	${WEB_MAKE} install


api-run-dev:
	${API_MAKE} run-dev

web-run-dev:
	${WEB_MAKE} run-dev
