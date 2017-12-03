(require 'url)

(defun advent-login (session)
  "Login to adventofcode.com"
  (interactive "sValue of session cookie from logged in browser: ")
  (url-cookie-store "session" session "Thu, 25 Dec 2027 20:17:36 -0000" ".adventofcode.com" "/" nil))

(defun advent (&optional day)
  "Loads todays adventofcode.com problem and input."
  (interactive)
  (let ((day (or day (advent-day))))
    (delete-other-windows)
    (split-window-right)
    (eww (format "http://adventofcode.com/2017/day/%d" day))
    (advent-input day)))

(defun advent-input (&optional day)
  "Loads todays adventofcode.com input in other window."
  (interactive)
  (let* ((day (or day (advent-day)))
         (url (format "http://adventofcode.com/2017/day/%d/input" day))
         (dir (format "/Users/keegan/src/advent/2017/%d" day))
         (file (format "%s/input" dir)))
    (if (not (file-exists-p file))
        (url-retrieve url 'advent-download-callback (list file))
      (find-file-other-window file))))

(defun advent-download-callback (status file)
  (if (plist-get status :error)
      (message "Failed to download todays advent %s" (plist-get status :error))
    (mkdir (file-name-directory file) t)
    (goto-char (point-min))
    (re-search-forward "\r?\n\r?\n")
    (write-region (point) (point-max) file)
    (find-file-other-window file)))

(defun advent-day ()
  (elt (decode-time (current-time)) 3))
